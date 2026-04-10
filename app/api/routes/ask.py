import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.core.logging import logger
from app.schemas.chat import AskRequest, AskResponse, CodeSuggestion, ErrorResponse
from app.services.graph import run_agent, run_agent_stream

router = APIRouter(prefix="/ask", tags=["QA"])


@router.post(
    "",
    response_model=AskResponse,
    response_model_exclude_none=True,
    responses={500: {"model": ErrorResponse}},
    summary="질문에 대한 답변 생성",
    description="XDWorld 메뉴얼 기반 RAG 질의응답 엔드포인트",
)
async def ask(req: AskRequest):
    try:
        result = run_agent(
            req.question,
            source_code=req.source_code,
            file_name=req.file_name,
            error_info=req.error_info
        )
        code_suggestions = None
        if result.get("code_suggestions"):
            code_suggestions = [
                CodeSuggestion(**cs) for cs in result["code_suggestions"]
            ]
        return AskResponse(
            answer=result["answer"],
            code_suggestions=code_suggestions,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        logger.error("질의 처리 실패: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail="답변 생성 중 오류가 발생했습니다.")


@router.post(
    "/stream",
    summary="질문에 대한 답변 생성 (Streaming)",
    description="LangGraph 노드 단계별 진행 상황을 SSE로 스트리밍",
)
async def ask_stream(req: AskRequest):
    async def event_generator():
        try:
            # 시작 이벤트
            yield f"data: {json.dumps({'type': 'start'}, ensure_ascii=False)}\n\n"
            
            # LangGraph 스트리밍
            async for event in run_agent_stream(
                req.question,
                source_code=req.source_code,
                file_name=req.file_name,
                error_info=req.error_info
            ):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
            
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
