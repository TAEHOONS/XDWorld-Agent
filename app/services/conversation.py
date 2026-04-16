import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Conversation, Message, MessageEmbedding
from app.db.redis_store import get_history, append_history
from app.services.embedding import summarize_message, generate_embedding
from app.core.logging import logger


def get_or_create_conversation(conversation_id: Optional[str], db: Session) -> tuple[str, list[dict]]:
    """
    대화 세션 조회 또는 생성.
    
    Returns:
        (conversation_id, history)
    """
    if conversation_id:
        # 기존 대화 확인
        conv = db.query(Conversation).filter(Conversation.id == uuid.UUID(conversation_id)).first()
        if not conv:
            logger.warning(f"존재하지 않는 conversation_id: {conversation_id}, 새로 생성")
            conversation_id = None
    
    if not conversation_id:
        # 새 대화 생성
        conv = Conversation()
        db.add(conv)
        db.commit()
        db.refresh(conv)
        conversation_id = str(conv.id)
        logger.info(f"새 대화 생성: {conversation_id}")
        return conversation_id, []
    
    # Redis에서 히스토리 조회
    history = get_history(conversation_id)
    return conversation_id, history


def save_message(conversation_id: str, role: str, content: str, db: Session):
    """메시지를 DB와 Redis에 저장하고, 요약 임베딩 생성"""
    msg = Message(
        conversation_id=uuid.UUID(conversation_id),
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    
    # Redis에도 저장
    append_history(conversation_id, role, content)
    
    # 요약 및 임베딩 생성 (비동기 처리 권장하지만 일단 동기로)
    try:
        summary = summarize_message(role, content)
        embedding_vector = generate_embedding(summary)
        
        embedding = MessageEmbedding(
            message_id=msg.id,
            summary=summary,
            embedding=embedding_vector
        )
        db.add(embedding)
        db.commit()
        logger.info(f"임베딩 저장 완료: {msg.id}")
    except Exception as e:
        logger.error(f"임베딩 저장 실패: {e}")
        # 임베딩 실패해도 메시지는 저장됨
    
    logger.info(f"메시지 저장 완료: {conversation_id} / {role}")


def search_similar_conversations(query: str, db: Session, limit: int = 5) -> list[dict]:
    """유사한 대화 검색 (pgvector)"""
    from sqlalchemy import text
    
    try:
        # 쿼리 임베딩 생성
        query_vector = generate_embedding(query)
        
        # pgvector cosine similarity 검색
        sql = text("""
            SELECT 
                m.id,
                m.role,
                m.content,
                me.summary,
                1 - (me.embedding <=> :query_vector) as similarity
            FROM message_embeddings me
            JOIN messages m ON me.message_id = m.id
            ORDER BY me.embedding <=> :query_vector
            LIMIT :limit
        """)
        
        result = db.execute(sql, {"query_vector": str(query_vector), "limit": limit})
        
        similar = []
        for row in result:
            similar.append({
                "message_id": str(row.id),
                "role": row.role,
                "content": row.content[:200],
                "summary": row.summary,
                "similarity": float(row.similarity)
            })
        
        logger.info(f"유사 대화 {len(similar)}개 검색 완료")
        return similar
        
    except Exception as e:
        logger.error(f"유사 대화 검색 실패: {e}")
        return []
