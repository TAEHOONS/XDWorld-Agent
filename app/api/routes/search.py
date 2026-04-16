from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.conversation import search_similar_conversations

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/similar")
async def search_similar(query: str, limit: int = 5, db: Session = Depends(get_db)):
    """유사한 대화 검색 (pgvector 기반)"""
    results = search_similar_conversations(query, db, limit)
    return {"query": query, "results": results}
