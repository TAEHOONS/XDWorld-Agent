"""검색 품질 향상을 위한 Query Expansion + Reranking"""

import re
from typing import List
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from app.core.config import get_settings
from app.core.logging import logger
from app.services.vectorstore import get_retriever


QUERY_EXPANSION_PROMPT = """사용자의 질문을 XDWorld 지도 엔진 메뉴얼 검색에 최적화된 형태로 재작성하세요.

원본 질문: {query}

다음 규칙을 따르세요:
1. 핵심 키워드 추출 (API 이름, 기능명)
2. 유사 표현 추가 (예: "카메라 이동" → "moveFront, moveCamera, 시점 변경")
3. 영문 API 이름이 있다면 포함
4. 한 줄로 간결하게

재작성된 질문:"""


def expand_query(query: str) -> str:
    """LLM을 사용해 검색 쿼리를 확장"""
    try:
        settings = get_settings()
        llm = ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0.0
        )
        
        prompt = QUERY_EXPANSION_PROMPT.format(query=query)
        response = llm.invoke(prompt)
        expanded = response.content.strip()
        
        logger.info(f"Query Expansion: '{query}' → '{expanded}'")
        return expanded
    except Exception as e:
        logger.warning(f"Query expansion 실패, 원본 사용: {e}")
        return query


def rerank_documents(query: str, docs: List[Document], top_k: int = 4) -> List[Document]:
    """문서를 관련도 기준으로 재순위화 (단일 LLM 배치 호출)"""
    if len(docs) <= top_k:
        return docs

    try:
        settings = get_settings()
        llm = ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0.0
        )

        doc_blocks = []
        for i, doc in enumerate(docs, start=1):
            doc_blocks.append(f"[{i}] {doc.page_content[:400]}")

        prompt = f"""질문: {query}

다음 문서들 중 질문과 가장 관련 있는 상위 {top_k}개를 골라 관련도 높은 순으로 번호를 나열하세요.

{chr(10).join(doc_blocks)}

응답 형식: 콤마로 구분된 번호만 출력. 예시) 3,7,1,9
다른 텍스트나 설명은 절대 포함하지 마세요."""

        response = llm.invoke(prompt)
        raw = response.content.strip()

        # 응답에서 정수만 추출 (LLM이 부가 텍스트를 섞어도 견고하게 파싱)
        nums = [int(n) for n in re.findall(r"\d+", raw)]
        # 1-based → 0-based, 유효 범위 + 중복 제거 (순서 유지)
        seen = set()
        indices = []
        for n in nums:
            idx = n - 1
            if 0 <= idx < len(docs) and idx not in seen:
                seen.add(idx)
                indices.append(idx)
            if len(indices) >= top_k:
                break

        if not indices:
            logger.warning(f"Reranking 응답 파싱 실패('{raw[:80]}'), 상위 {top_k}개 반환")
            return docs[:top_k]

        reranked = [docs[i] for i in indices]
        # top_k에 못 미치면 남은 문서로 채움 (원래 순서 유지)
        if len(reranked) < top_k:
            for i, doc in enumerate(docs):
                if i not in seen:
                    reranked.append(doc)
                    if len(reranked) >= top_k:
                        break

        logger.info(f"Reranking: {len(docs)}개 → {len(reranked)}개 선택 (순서: {indices})")
        return reranked

    except Exception as e:
        logger.warning(f"Reranking 실패, 상위 {top_k}개 반환: {e}")
        return docs[:top_k]


def search_with_enhancement(query: str) -> List[Document]:
    """Query Expansion + 검색 + Reranking 파이프라인"""
    settings = get_settings()
    
    # 1. Query Expansion
    expanded_query = expand_query(query)
    
    # 2. 벡터 검색 (k=10)
    retriever = get_retriever(k=settings.retriever_k)
    docs = retriever.invoke(expanded_query)
    
    logger.info(f"검색 완료: {len(docs)}개 문서")
    
    # 3. Reranking (상위 4개 선택)
    reranked_docs = rerank_documents(expanded_query, docs, top_k=settings.rerank_top_k)
    
    return reranked_docs
