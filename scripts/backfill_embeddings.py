"""기존 메시지에 임베딩 추가하는 스크립트"""
import sys
sys.path.insert(0, '.')

from app.db.database import init_db, get_db
from app.db.models import Message, MessageEmbedding
from app.services.embedding import summarize_message, generate_embedding
from app.core.logging import logger

init_db()

db = next(get_db())

# 임베딩 없는 메시지 조회
messages = db.query(Message).outerjoin(MessageEmbedding).filter(MessageEmbedding.id == None).all()

logger.info(f"임베딩 생성 대상: {len(messages)}개 메시지")

for msg in messages:
    try:
        summary = summarize_message(msg.role, msg.content)
        embedding_vector = generate_embedding(summary)
        
        embedding = MessageEmbedding(
            message_id=msg.id,
            summary=summary,
            embedding=embedding_vector
        )
        db.add(embedding)
        db.commit()
        logger.info(f"✓ {msg.id} - {summary[:50]}")
    except Exception as e:
        logger.error(f"✗ {msg.id} - {e}")

logger.info("완료!")
