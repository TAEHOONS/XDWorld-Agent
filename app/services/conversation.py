import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.db.database import _session_factory  # noqa: F401  (런타임에 init_db 이후 채워짐)
from app.db import database as _db_module
from app.db.models import Conversation, Message, MessageEmbedding
from app.db.redis_store import get_history, append_history
from app.services.embedding import summarize_message, generate_embedding
from app.core.logging import logger


def get_or_create_conversation(conversation_id: Optional[str], user_id: str, db: Session) -> tuple[str, list[dict]]:
    """
    대화 세션 조회 또는 생성.
    
    Returns:
        (conversation_id, history)
    """
    if conversation_id:
        # 기존 대화 확인 (user_id도 검증)
        conv = db.query(Conversation).filter(
            Conversation.id == uuid.UUID(conversation_id),
            Conversation.user_id == user_id
        ).first()
        if not conv:
            logger.warning(f"존재하지 않거나 권한 없는 conversation_id: {conversation_id}, 새로 생성")
            conversation_id = None
    
    if not conversation_id:
        # 새 대화 생성
        conv = Conversation(user_id=user_id)
        db.add(conv)
        db.commit()
        db.refresh(conv)
        conversation_id = str(conv.id)
        logger.info(f"새 대화 생성: {conversation_id} (user: {user_id})")
        return conversation_id, []
    
    # Redis에서 히스토리 조회
    history = get_history(conversation_id)
    return conversation_id, history


def save_message(conversation_id: str, role: str, content: str, db: Session) -> uuid.UUID:
    """메시지를 DB와 Redis에 저장하고 message_id 반환. 임베딩은 백그라운드에서 처리."""
    msg = Message(
        conversation_id=uuid.UUID(conversation_id),
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)

    append_history(conversation_id, role, content)
    logger.info(f"메시지 저장 완료: {conversation_id} / {role}")
    return msg.id


def create_embedding_for_message(
    message_id: uuid.UUID,
    role: str,
    content: str,
    user_id: Optional[str] = None,
    conversation_id: Optional[str] = None,
) -> None:
    """LLM 요약 + 임베딩 + 저장. BackgroundTasks에서 호출 (별도 DB 세션 사용).

    user_id가 있으면 요약·임베딩 토큰 사용량도 함께 기록한다.
    """
    try:
        summary = summarize_message(role, content, user_id, conversation_id)
        embedding_vector = generate_embedding(summary, user_id, conversation_id)
    except Exception as e:
        logger.error(f"임베딩 생성 실패 (message_id={message_id}): {e}")
        return

    if _db_module._session_factory is None:
        logger.error("세션 팩토리 미초기화 - 임베딩 저장 스킵")
        return

    with _db_module._session_factory() as session:
        try:
            session.add(MessageEmbedding(
                message_id=message_id,
                summary=summary,
                embedding=embedding_vector
            ))
            session.commit()
            logger.info(f"임베딩 저장 완료: {message_id}")
        except Exception as e:
            session.rollback()
            logger.error(f"임베딩 저장 실패 (message_id={message_id}): {e}")


def search_similar_conversations(query: str, user_id: str, db: Session, limit: int = 5) -> list[dict]:
    """유사한 대화 검색 (pgvector) - 사용자별 격리"""
    from sqlalchemy import text
    
    try:
        # 쿼리 임베딩 생성 (사용량은 해당 user_id로 기록)
        query_vector = generate_embedding(query, user_id=user_id)
        
        # pgvector cosine similarity 검색 (user_id 필터 추가)
        sql = text("""
            SELECT 
                m.id,
                m.role,
                m.content,
                me.summary,
                1 - (me.embedding <=> :query_vector) as similarity
            FROM message_embeddings me
            JOIN messages m ON me.message_id = m.id
            JOIN conversations c ON m.conversation_id = c.id
            WHERE c.user_id = :user_id
            ORDER BY me.embedding <=> :query_vector
            LIMIT :limit
        """)
        
        result = db.execute(sql, {
            "query_vector": str(query_vector), 
            "user_id": user_id,
            "limit": limit
        })
        
        similar = []
        for row in result:
            similar.append({
                "message_id": str(row.id),
                "role": row.role,
                "content": row.content[:200],
                "summary": row.summary,
                "similarity": float(row.similarity)
            })
        
        logger.info(f"유사 대화 {len(similar)}개 검색 완료 (user: {user_id})")
        return similar
        
    except Exception as e:
        logger.error(f"유사 대화 검색 실패: {e}")
        return []
