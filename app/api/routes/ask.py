import json
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.logging import logger
from app.core.auth import get_current_user
from app.schemas.chat import (
    AskRequest, AskResponse, AskAsyncResponse, ResultResponse,
    CodeSuggestion, ErrorResponse, InterruptedResponse
)
from app.services.graph import run_agent, run_agent_stream, resume_agent, resume_agent_stream
from app.services.conversation import (
    get_or_create_conversation,
    save_message,
    create_embedding_for_message,
)
from app.db.database import get_db
from app.db.redis_store import create_request_id, save_result, get_result, publish_result

router = APIRouter(prefix="/ask", tags=["QA"])


@router.post(
    "",
    responses={
        200: {"model": AskResponse},
        202: {"model": InterruptedResponse},
        500: {"model": ErrorResponse}
    },
    summary="질문에 대한 답변 생성",
    description="XDWorld 메뉴얼 기반 RAG 질의응답 엔드포인트. 코드 생성 요청 시 Human-in-the-Loop으로 중단될 수 있음.",
)
async def ask(
    req: AskRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        # 대화 세션 조회/생성 및 히스토리 가져오기
        conversation_id, history = get_or_create_conversation(req.conversation_id, user_id, db)

        # 사용자 메시지 저장 (임베딩은 백그라운드로)
        user_msg_id = save_message(conversation_id, "user", req.question, db)
        background_tasks.add_task(create_embedding_for_message, user_msg_id, "user", req.question)

        # Agent 실행
        result = run_agent(
            req.question,
            source_code=req.source_code,
            file_name=req.file_name,
            error_info=req.error_info,
            history=history,
            db=db,
            user_id=user_id
        )

        # Human-in-the-Loop 중단 체크
        if result.get("interrupted"):
            return InterruptedResponse(
                thread_id=result["thread_id"],
                conversation_id=conversation_id,
                context=result.get("context", ""),
                intent=result.get("intent", ""),
                next_node=result.get("next_node")
            )

        # Assistant 응답 저장 (임베딩은 백그라운드로)
        assistant_msg_id = save_message(conversation_id, "assistant", result["answer"], db)
        background_tasks.add_task(create_embedding_for_message, assistant_msg_id, "assistant", result["answer"])
        
        code_suggestions = None
        if result.get("code_suggestions"):
            code_suggestions = [
                CodeSuggestion(**cs) for cs in result["code_suggestions"]
            ]
        
        return AskResponse(
            conversation_id=conversation_id,
            answer=result["answer"],
            code_suggestions=code_suggestions,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        logger.error("질의 처리 실패: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail="답변 생성 중 오류가 발생했습니다.")


@router.post(
    "/resume",
    summary="중단된 Agent 재개 (SSE)",
    description="코드 생성 전 중단된 상태를 사용자 승인 후 SSE 스트리밍으로 재개",
)
async def resume(
    thread_id: str,
    approved: bool = True,
    additional_context: str = None,
    db: Session = Depends(get_db)
):
    async def event_generator():
        try:
            async for event in resume_agent_stream(thread_id, approved, additional_context):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
            yield f"data: {json.dumps({'type': 'done'}, ensure_ascii=False)}\n\n"
        except ValueError as exc:
            yield f"data: {json.dumps({'type': 'error', 'message': str(exc)}, ensure_ascii=False)}\n\n"
        except Exception as exc:
            logger.error("재개 실패: %s", exc, exc_info=True)
            yield f"data: {json.dumps({'type': 'error', 'message': '재개 중 오류가 발생했습니다.'}, ensure_ascii=False)}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@router.post(
    "/stream",
    summary="질문에 대한 답변 생성 (Streaming)",
    description="LangGraph 노드 단계별 진행 상황을 SSE로 스트리밍",
)
async def ask_stream(
    req: AskRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    async def event_generator():
        try:
            # 대화 세션 조회/생성
            conversation_id, history = get_or_create_conversation(req.conversation_id, user_id, db)

            # 사용자 메시지 저장 (임베딩은 백그라운드로)
            user_msg_id = save_message(conversation_id, "user", req.question, db)
            background_tasks.add_task(create_embedding_for_message, user_msg_id, "user", req.question)

            # 시작 이벤트 (conversation_id 포함)
            yield f"data: {json.dumps({'type': 'start', 'conversation_id': conversation_id}, ensure_ascii=False)}\n\n"

            collected_answer = ""
            interrupted = False

            # LangGraph 스트리밍
            async for event in run_agent_stream(
                req.question,
                source_code=req.source_code,
                file_name=req.file_name,
                error_info=req.error_info,
                history=history,
                thread_id=req.conversation_id,
                db=db,
                user_id=user_id
            ):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"

                # 중단 체크
                if event.get("type") == "interrupted":
                    interrupted = True
                    break

                # 최종 답변 수집
                if event.get("type") == "result":
                    collected_answer = event.get("answer", "")

            # 중단되지 않았으면 Assistant 응답 저장 (임베딩은 백그라운드로)
            if not interrupted and collected_answer:
                assistant_msg_id = save_message(conversation_id, "assistant", collected_answer, db)
                background_tasks.add_task(create_embedding_for_message, assistant_msg_id, "assistant", collected_answer)
            
            # 완료 이벤트
            if not interrupted:
                yield f"data: {json.dumps({'type': 'done'}, ensure_ascii=False)}\n\n"
            
        except ValueError as exc:
            yield f"data: {json.dumps({'type': 'error', 'message': str(exc)}, ensure_ascii=False)}\n\n"
        except Exception as exc:
            logger.error("스트리밍 실패: %s", exc, exc_info=True)
            yield f"data: {json.dumps({'type': 'error', 'message': '답변 생성 중 오류가 발생했습니다.'}, ensure_ascii=False)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


async def _process_ask_background(
    request_id: str,
    req: AskRequest,
    conversation_id: str,
    history: list,
    db: Session,
    user_id: str
):
    """백그라운드에서 질의 처리"""
    try:
        result = run_agent(
            req.question,
            source_code=req.source_code,
            file_name=req.file_name,
            error_info=req.error_info,
            history=history,
            db=db,
            user_id=user_id
        )
        
        if result.get("interrupted"):
            response = {
                "status": "interrupted",
                "thread_id": result["thread_id"],
                "conversation_id": conversation_id,
                "context": result.get("context", ""),
                "intent": result.get("intent", ""),
            }
        else:
            assistant_msg_id = save_message(conversation_id, "assistant", result["answer"], db)
            # 이미 백그라운드 컨텍스트이므로 동기 호출 (응답 경로 영향 없음)
            create_embedding_for_message(assistant_msg_id, "assistant", result["answer"])
            response = {
                "status": "completed",
                "request_id": request_id,
                "conversation_id": conversation_id,
                "answer": result["answer"],
                "code_suggestions": result.get("code_suggestions"),
            }
        
        save_result(request_id, response)
        publish_result(request_id, response)
        
    except Exception as exc:
        logger.error("백그라운드 처리 실패: %s", exc, exc_info=True)
        error_response = {
            "status": "error",
            "request_id": request_id,
            "error": str(exc)
        }
        save_result(request_id, error_response)
        publish_result(request_id, error_response)


@router.post(
    "/async",
    response_model=AskAsyncResponse,
    summary="질문 비동기 제출 (Redis Pub/Sub)",
    description="질문을 제출하고 즉시 request_id를 반환. 결과는 /ask/result/{request_id}로 조회",
)
async def ask_async(
    req: AskRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    try:
        request_id = create_request_id()
        conversation_id, history = get_or_create_conversation(req.conversation_id, user_id, db)
        user_msg_id = save_message(conversation_id, "user", req.question, db)
        background_tasks.add_task(create_embedding_for_message, user_msg_id, "user", req.question)

        # 백그라운드 작업 등록
        background_tasks.add_task(
            _process_ask_background,
            request_id,
            req,
            conversation_id,
            history,
            db,
            user_id
        )
        
        return AskAsyncResponse(
            request_id=request_id,
            conversation_id=conversation_id,
            status="processing"
        )
    except Exception as exc:
        logger.error("비동기 요청 실패: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail=str(exc))


@router.get(
    "/result/{request_id}",
    response_model=ResultResponse,
    summary="비동기 요청 결과 조회",
    description="request_id로 처리 결과 조회",
)
async def get_ask_result(request_id: str):
    result = get_result(request_id)
    
    if not result:
        return ResultResponse(
            request_id=request_id,
            status="processing"
        )
    
    # result에 request_id가 없으면 추가
    if "request_id" not in result:
        result["request_id"] = request_id
    
    return ResultResponse(**result)
