from fastapi import APIRouter

from app.api.routes.ask import router as ask_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(ask_router)
