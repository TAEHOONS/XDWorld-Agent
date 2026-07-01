import uuid
from datetime import datetime
from decimal import Decimal

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, ForeignKey, Index, Integer, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Conversation(Base):
    """대화 세션"""
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    messages: Mapped[list["Message"]] = relationship(back_populates="conversation", order_by="Message.created_at")


class Message(Base):
    """원본 메시지 전체 저장 (PostgreSQL)"""
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("conversations.id", ondelete="CASCADE"))
    role: Mapped[str] = mapped_column(String(20))   # "user" | "assistant"
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    conversation: Mapped["Conversation"] = relationship(back_populates="messages")
    embedding: Mapped["MessageEmbedding"] = relationship(back_populates="message", uselist=False)


class MessageEmbedding(Base):
    """압축 요약 벡터 저장 (pgvector) - 유사 대화 검색용"""
    __tablename__ = "message_embeddings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("messages.id", ondelete="CASCADE"), unique=True)
    summary: Mapped[str] = mapped_column(Text)           # 압축 요약 텍스트
    embedding: Mapped[list[float]] = mapped_column(Vector(1536))  # text-embedding-3-small 차원

    message: Mapped["Message"] = relationship(back_populates="embedding")


class TokenUsage(Base):
    """사용자별 LLM 토큰 사용량 1건(=1 LLM 호출). 일별/누적 집계와 향후 한도(quota) 산정의 원장."""
    __tablename__ = "token_usage"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    # 과금 이력은 대화 삭제와 독립적으로 보존해야 하므로 FK/CASCADE를 걸지 않는다.
    conversation_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    kind: Mapped[str] = mapped_column(String(20), nullable=False)  # "chat" | "summary" | "embedding"
    input_tokens: Mapped[int] = mapped_column(Integer, default=0)
    output_tokens: Mapped[int] = mapped_column(Integer, default=0)
    total_tokens: Mapped[int] = mapped_column(Integer, default=0)
    # 사용 시점 단가로 산정한 예상 비용(USD). 단가가 바뀌어도 과거 비용은 보존된다.
    cost_usd: Mapped[Decimal] = mapped_column(Numeric(12, 6), default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # 일별 리셋 한도 조회( user_id + 날짜 범위 )를 위한 복합 인덱스
    __table_args__ = (
        Index("ix_token_usage_user_created", "user_id", "created_at"),
    )
