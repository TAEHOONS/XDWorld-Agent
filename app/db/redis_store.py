import json

import redis

from app.core.config import get_settings

_redis: redis.Redis | None = None
TTL = 60 * 60 * 24  # 24시간


def init_redis():
    global _redis
    settings = get_settings()
    _redis = redis.from_url(settings.redis_url, decode_responses=True)


def get_redis() -> redis.Redis:
    return _redis


def get_history(conversation_id: str) -> list[dict]:
    """Redis에서 대화 히스토리 조회"""
    data = _redis.get(f"history:{conversation_id}")
    return json.loads(data) if data else []


def append_history(conversation_id: str, role: str, content: str):
    """Redis 히스토리에 메시지 추가"""
    key = f"history:{conversation_id}"
    history = get_history(conversation_id)
    history.append({"role": role, "content": content})
    _redis.setex(key, TTL, json.dumps(history, ensure_ascii=False))
