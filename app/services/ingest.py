"""Markdown 문서를 벡터스토어로 인제스트하는 모듈."""

from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from app.core.config import get_settings
from app.core.exceptions import DocumentLoadError
from app.core.logging import logger
from app.services.vectorstore import get_embeddings

_ENCODINGS = ("utf-8", "utf-8-sig", "cp949", "euc-kr")


def _read_file(file_path: Path) -> str:
    for enc in _ENCODINGS:
        try:
            return file_path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    raise DocumentLoadError(f"지원된 인코딩으로 읽을 수 없습니다: {file_path}")


def load_markdown_documents() -> list[Document]:
    settings = get_settings()
    raw_dir = Path(settings.raw_md_dir)

    if not raw_dir.exists():
        raise DocumentLoadError(f"MD 폴더가 없습니다: {raw_dir}")

    md_files = list(raw_dir.rglob("*.md"))
    if not md_files:
        raise DocumentLoadError("로드할 MD 문서가 없습니다.")

    docs: list[Document] = []
    failed = 0

    for fp in md_files:
        try:
            text = _read_file(fp)
            relative = str(fp.relative_to(raw_dir)).replace("\\", "/")
            docs.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": str(fp),
                        "file_name": fp.name,
                        "folder": fp.parent.name,
                        "relative_path": relative,
                    },
                )
            )
        except Exception as exc:
            logger.warning("문서 로드 실패: %s -> %s", fp, exc)
            failed += 1

    if not docs:
        raise DocumentLoadError("문서를 하나도 읽지 못했습니다.")

    logger.info("문서 로드 완료: %d건 (실패: %d건)", len(docs), failed)
    return docs


def split_documents(
    docs: list[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = splitter.split_documents(docs)
    logger.info("청크 분할 완료: %d건", len(chunks))
    return chunks


def build_and_save_vectorstore(chunks: list[Document]) -> None:
    settings = get_settings()

    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")

    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    save_path = Path(settings.vectorstore_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(save_path))
    logger.info("벡터스토어 저장 완료: %s", save_path)


def ingest() -> None:
    """전체 인제스트 파이프라인을 실행합니다."""
    logger.info("=== 인제스트 시작 ===")
    docs = load_markdown_documents()
    chunks = split_documents(docs)
    build_and_save_vectorstore(chunks)
    logger.info("=== 인제스트 완료 ===")


if __name__ == "__main__":
    ingest()
