"""벡터스토어 싱글턴 관리 모듈."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from app.core.config import get_settings
from app.core.exceptions import VectorStoreNotFoundError
from app.core.logging import logger

_vectorstore: Optional[FAISS] = None


def get_embeddings() -> OpenAIEmbeddings:
    settings = get_settings()
    return OpenAIEmbeddings(api_key=settings.openai_api_key)


def load_vectorstore(*, force_reload: bool = False) -> FAISS:
    """벡터스토어를 로드하고 캐싱합니다. 앱 수명 동안 한 번만 로드됩니다."""
    global _vectorstore

    if _vectorstore is not None and not force_reload:
        return _vectorstore

    settings = get_settings()
    vs_path = Path(settings.vectorstore_dir)

    if not vs_path.exists():
        raise VectorStoreNotFoundError(
            f"벡터스토어 경로가 존재하지 않습니다: {vs_path}. "
            "먼저 `python -m app.services.ingest` 를 실행하세요."
        )

    logger.info("벡터스토어 로드 중: %s", vs_path)
    _vectorstore = FAISS.load_local(
        str(vs_path),
        get_embeddings(),
        allow_dangerous_deserialization=True,
    )
    logger.info("벡터스토어 로드 완료")
    return _vectorstore


def get_retriever(k: Optional[int] = None):
    settings = get_settings()
    vs = load_vectorstore()
    return vs.as_retriever(search_kwargs={"k": k or settings.retriever_k})
