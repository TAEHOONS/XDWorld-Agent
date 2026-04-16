"""메시지 요약 및 임베딩 생성"""
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.core.config import get_settings
from app.core.logging import logger


def summarize_message(role: str, content: str) -> str:
    """메시지를 한 줄로 요약"""
    settings = get_settings()
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=settings.openai_api_key,
        temperature=0.0
    )
    
    prompt = f"""다음 {role} 메시지를 핵심만 담아 한 문장으로 요약하세요.

메시지:
{content[:500]}

요약:"""
    
    try:
        response = llm.invoke(prompt)
        summary = response.content.strip()
        logger.info(f"요약 생성: {summary[:50]}...")
        return summary
    except Exception as e:
        logger.error(f"요약 생성 실패: {e}")
        # 실패 시 원본 앞부분 사용
        return content[:100]


def generate_embedding(text: str) -> list[float]:
    """텍스트를 벡터로 변환"""
    settings = get_settings()
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=settings.openai_api_key
    )
    
    try:
        vector = embeddings.embed_query(text)
        logger.info(f"임베딩 생성 완료: {len(vector)}차원")
        return vector
    except Exception as e:
        logger.error(f"임베딩 생성 실패: {e}")
        raise
