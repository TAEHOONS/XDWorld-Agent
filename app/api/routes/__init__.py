from fastapi import APIRouter

from app.api.routes.ask import router as ask_router
from app.api.routes.search import router as search_router
from app.api.routes.usage import router as usage_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(ask_router)
api_router.include_router(search_router)
api_router.include_router(usage_router)
