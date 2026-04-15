import os
os.environ.setdefault("PGCLIENTENCODING", "utf8")

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from typing import Generator

from app.core.config import get_settings


class Base(DeclarativeBase):
    pass


_engine = None
_session_factory = None


def init_db():
    global _engine, _session_factory
    get_settings.cache_clear()
    settings = get_settings()
    raw_url = settings.database_url.replace("postgresql+asyncpg://", "postgresql+psycopg2://")
    # psycopg2가 Windows CP949로 URL을 읽는 문제 방지 — bytes로 강제 변환
    url = raw_url.encode("utf-8").decode("utf-8")
    _engine = create_engine(url, echo=False)
    _session_factory = sessionmaker(_engine, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    with _session_factory() as session:
        yield session


def create_tables():
    from app.core.logging import logger
    logger.info("테이블 생성 시작")
    with _engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        logger.info("pgvector extension 활성화 완료")
    Base.metadata.create_all(_engine)
    logger.info("테이블 생성 완료")
