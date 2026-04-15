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
    retriever_k: int = 4

    # Database
    database_url: str = "postgresql+asyncpg://xdworld:xdworld@localhost:5432/xdworld_agent"

    # Redis
    redis_url: str = "redis://localhost:6379"

    # App
    app_title: str = "XDWorld Agent"
    app_version: str = "1.0.0"
    cors_origins: List[str] = ["*"]
    log_level: str = "INFO"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()
