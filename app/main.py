from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.core.config import get_settings
from app.core.logging import logger
from app.api.routes import api_router
from app.services.vectorstore import load_vectorstore
from app.db.database import init_db, create_tables
from app.db.redis_store import init_redis
from app.db.models import Conversation, Message, MessageEmbedding  # 명시적 import
import app.services.graph as graph_module

STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("앱 시작 - 초기화 중")
    init_db()
    init_redis()
    create_tables()
    try:
        load_vectorstore()
    except Exception as exc:
        logger.warning("벡터스토어 사전 로드 실패: %s", exc)
    try:
        graph_module._graph_streaming = await graph_module._build_graph_streaming()
        logger.info("스트리밍 그래프 초기화 완료")
    except Exception as exc:
        logger.warning("스트리밍 그래프 초기화 실패: %s", exc)
    yield
    logger.info("앱 종료")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_title,
        version=settings.app_version,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS: "*" + credentials=True 조합은 브라우저가 거부하므로 자동 다운그레이드.
    origins = settings.cors_origins or []
    use_wildcard = "*" in origins or not origins
    if use_wildcard:
        logger.warning(
            "CORS_ORIGINS 미설정 또는 '*' 사용 - credentials 비활성화. 운영에선 도메인 명시 권장."
        )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins if origins else ["*"],
        allow_credentials=not use_wildcard,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

    @app.get("/", include_in_schema=False)
    async def index():
        return FileResponse(str(STATIC_DIR / "index.html"))

    @app.get("/health", tags=["Health"])
    async def health():
        return {"status": "ok", "version": settings.app_version}

    return app


app = create_app()
