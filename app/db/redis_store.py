import json
import uuid

import redis

from app.core.config import get_settings

_redis: redis.Redis | None = None
TTL = 60 * 60 * 24  # 24시간
RESULT_TTL = 60 * 10  # 10분


def init_redis():
    global _redis
    settings = get_settings()

    if settings.active_profile == "local":
        # 로컬: 단일 노드 URL
        _redis = redis.from_url(settings.redis_host, decode_responses=True)
    else:
        # 운영: 회사 Redis (egis-llm-worker 패턴, 클러스터 proxy 앞단)
        _redis = redis.Redis(
            host=settings.redis_host_1,
            port=settings.redis_port,
            username=settings.redis_username or None,
            password=settings.redis_password or None,
            socket_timeout=10,
            decode_responses=True,
        )


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


def create_request_id() -> str:
    """고유 요청 ID 생성"""
    return str(uuid.uuid4())


def save_result(request_id: str, result: dict):
    """처리 결과를 Redis에 저장"""
    key = f"result:{request_id}"
    _redis.setex(key, RESULT_TTL, json.dumps(result, ensure_ascii=False))


def get_result(request_id: str) -> dict | None:
    """처리 결과 조회"""
    data = _redis.get(f"result:{request_id}")
    return json.loads(data) if data else None


def publish_result(request_id: str, result: dict):
    """Pub/Sub으로 결과 발행"""
    channel = f"result:{request_id}"
    _redis.publish(channel, json.dumps(result, ensure_ascii=False))
