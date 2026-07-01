"""메시지 요약 및 임베딩 생성"""
from typing import Optional

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.core.config import get_settings
from app.core.logging import logger

_SUMMARY_MODEL = "gpt-4o-mini"
_EMBEDDING_MODEL = "text-embedding-3-small"


def summarize_message(
    role: str,
    content: str,
    user_id: Optional[str] = None,
    conversation_id: Optional[str] = None,
) -> str:
    """메시지를 한 줄로 요약. user_id가 있으면 토큰 사용량을 기록한다."""
    settings = get_settings()
    llm = ChatOpenAI(
        model=_SUMMARY_MODEL,
        api_key=settings.openai_api_key,
        temperature=0.0
    )

    prompt = f"""다음 {role} 메시지를 핵심만 담아 한 문장으로 요약하세요.

메시지:
{content[:500]}

요약:"""

    try:
        response = llm.invoke(prompt)
        if user_id:
            from app.services.usage import record_usage
            um = getattr(response, "usage_metadata", None) or {}
            record_usage(
                user_id, _SUMMARY_MODEL,
                um.get("input_tokens", 0), um.get("output_tokens", 0),
                "summary", conversation_id,
            )
        summary = response.content.strip()
        logger.info(f"요약 생성: {summary[:50]}...")
        return summary
    except Exception as e:
        logger.error(f"요약 생성 실패: {e}")
        # 실패 시 원본 앞부분 사용
        return content[:100]


def generate_embedding(
    text: str,
    user_id: Optional[str] = None,
    conversation_id: Optional[str] = None,
) -> list[float]:
    """텍스트를 벡터로 변환. user_id가 있으면 토큰 사용량을 기록한다."""
    settings = get_settings()
    embeddings = OpenAIEmbeddings(
        model=_EMBEDDING_MODEL,
        api_key=settings.openai_api_key
    )

    try:
        vector = embeddings.embed_query(text)
        if user_id:
            from app.services.usage import count_tokens, record_usage
            # 임베딩은 usage를 반환하지 않으므로 tiktoken으로 입력 토큰을 계산(출력 토큰 없음)
            record_usage(
                user_id, _EMBEDDING_MODEL,
                count_tokens(text, _EMBEDDING_MODEL), 0,
                "embedding", conversation_id,
            )
        logger.info(f"임베딩 생성 완료: {len(vector)}차원")
        return vector
    except Exception as e:
        logger.error(f"임베딩 생성 실패: {e}")
        raise
