from __future__ import annotations

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # OpenAI
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.0

    # Vectorstore
    raw_md_dir: str = "data/raw_md"
    vectorstore_dir: str = "data/vectorstore"
    retriever_k: int = 10
    rerank_top_k: int = 4

    # Database
    # 로컬(ACTIVE_PROFILE=local): DATABASE_URL_LOCAL 사용
    # 운영(ACTIVE_PROFILE=prod):  DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD 조합
    database_url_local: str = "postgresql+asyncpg://xdworld:xdworld@localhost:5432/xdworld_agent"
    db_host: str = ""
    db_port: int = 5432
    db_name: str = ""
    db_user: str = ""
    db_password: str = ""

    # Profile (local: 로컬 단일 Redis, prod: 회사 Redis 클러스터)
    active_profile: str = "local"

    # Redis
    redis_host: str = "redis://localhost:6379"
    redis_host_1: str = ""
    redis_host_2: str = ""
    redis_port: int = 6379
    redis_username: str = ""
    redis_password: str = ""

    # App
    app_title: str = "XDWorld Agent"
    app_version: str = "1.0.0"
    # CORS_ORIGINS는 콤마/JSON 리스트로 운영 도메인을 명시.
    # 비워두면 "*" + credentials=True 조합으로 브라우저가 거부하므로 운영 배포 전 반드시 설정.
    cors_origins: List[str] = []
    log_level: str = "INFO"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
