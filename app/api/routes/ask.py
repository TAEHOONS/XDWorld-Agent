import json
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.core.logging import logger
from app.schemas.chat import AskRequest, AskResponse, CodeSuggestion, ErrorResponse, InterruptedResponse
from app.services.graph import run_agent, run_agent_stream, resume_agent
from app.services.conversation import get_or_create_conversation, save_message
from app.db.database import get_db

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
async def ask(req: AskRequest, db: Session = Depends(get_db)):
    try:
        # 대화 세션 조회/생성 및 히스토리 가져오기
        conversation_id, history = get_or_create_conversation(req.conversation_id, db)
        
        # 사용자 메시지 저장
        save_message(conversation_id, "user", req.question, db)
        
        # Agent 실행
        result = run_agent(
            req.question,
            source_code=req.source_code,
            file_name=req.file_name,
            error_info=req.error_info,
            history=history
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
        
        # Assistant 응답 저장
        save_message(conversation_id, "assistant", result["answer"], db)
        
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
    response_model=AskResponse,
    response_model_exclude_none=True,
    summary="중단된 Agent 재개 (Human-in-the-Loop)",
    description="코드 생성 전 중단된 상태를 사용자 승인 후 재개",
)
async def resume(
    thread_id: str,
    approved: bool = True,
    additional_context: str = None,
    db: Session = Depends(get_db)
):
    try:
        result = resume_agent(thread_id, approved, additional_context)
        
        code_suggestions = None
        if result.get("code_suggestions"):
            code_suggestions = [
                CodeSuggestion(**cs) for cs in result["code_suggestions"]
            ]
        
        return AskResponse(
            conversation_id=thread_id,
            answer=result["answer"],
            code_suggestions=code_suggestions,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        logger.error("재개 실패: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail="재개 중 오류가 발생했습니다.")


@router.post(
    "/stream",
    summary="질문에 대한 답변 생성 (Streaming)",
    description="LangGraph 노드 단계별 진행 상황을 SSE로 스트리밍",
)
async def ask_stream(req: AskRequest, db: Session = Depends(get_db)):
    async def event_generator():
        try:
            # 대화 세션 조회/생성
            conversation_id, history = get_or_create_conversation(req.conversation_id, db)
            
            # 사용자 메시지 저장
            save_message(conversation_id, "user", req.question, db)
            
            # 시작 이벤트 (conversation_id 포함)
            yield f"data: {json.dumps({'type': 'start', 'conversation_id': conversation_id}, ensure_ascii=False)}\n\n"
            
            collected_answer = ""
            
            # LangGraph 스트리밍
            async for event in run_agent_stream(
                req.question,
                source_code=req.source_code,
                file_name=req.file_name,
                error_info=req.error_info,
                history=history
            ):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
                
                # 최종 답변 수집
                if event.get("type") == "result":
                    collected_answer = event.get("answer", "")
            
            # Assistant 응답 저장
            if collected_answer:
                save_message(conversation_id, "assistant", collected_answer, db)
            
            # 완료 이벤트
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
