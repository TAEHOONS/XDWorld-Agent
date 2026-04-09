from fastapi import APIRouter, HTTPException

from app.core.logging import logger
from app.schemas.chat import AskRequest, AskResponse, CodeSuggestion, ErrorResponse
from app.services.graph import run_agent

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
        result = run_agent(req.question)
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
