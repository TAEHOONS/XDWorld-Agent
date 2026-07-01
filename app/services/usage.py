"""LLM 토큰 사용량 측정·기록.

한 번의 사용자 질문에서 발생하는 모든 LLM 호출의 토큰을 사용자별로 적재한다.

포착 경로
  - 그래프 내부 chat 호출(intent 폴백 / query expansion / reranking / 최종 답변):
    UsageCollector 콜백을 graph config에 부착해 한 번에 포착한다.
  - 백그라운드 요약 chat + 메시지/유사검색 임베딩: 각 호출부에서 record_usage로 직접 기록.

알려진 제외(비용 무시 수준): FAISS 벡터 검색용 쿼리 임베딩.
  → text-embedding-3-small($0.02/1M)에 쿼리 수십 토큰 수준이라 그래프 내부 retriever
    내부에서 발생하며 user_id 전파가 어려워 제외한다. 필요 시 별도 작업으로 추가.
"""
from __future__ import annotations

import uuid
from decimal import Decimal
from typing import Optional, Union

from langchain_core.callbacks import BaseCallbackHandler

from app.core.config import get_settings
from app.core.logging import logger


# 모델별 단가 (USD / 1M tokens). OpenAI 공시가 기준(2026-06).
# 새 모델은 여기에 추가. 미등록 모델은 비용 0으로 기록되고 1회 경고 로그를 남긴다.
PRICING: dict[str, dict[str, float]] = {
    "gpt-4o-mini":            {"input": 0.15, "output": 0.60},
    "gpt-4o":                 {"input": 2.50, "output": 10.00},
    "gpt-4.1-mini":           {"input": 0.40, "output": 1.60},
    "gpt-4.1":                {"input": 2.00, "output": 8.00},
    "text-embedding-3-small": {"input": 0.02, "output": 0.0},
    "text-embedding-3-large": {"input": 0.13, "output": 0.0},
}

_warned_models: set[str] = set()
_PER_MILLION = Decimal(1_000_000)


def _normalize_model(model: str) -> str:
    """'gpt-4o-mini-2024-07-18'처럼 날짜 접미사가 붙은 모델명을 단가표 키로 정규화."""
    if model in PRICING:
        return model
    # 가장 긴 prefix 매칭
    for key in sorted(PRICING, key=len, reverse=True):
        if model.startswith(key):
            return key
    return model


def compute_cost(model: str, input_tokens: int, output_tokens: int) -> Decimal:
    """사용 시점 단가로 예상 비용(USD)을 계산. 미등록 모델은 0(경고 1회)."""
    key = _normalize_model(model)
    price = PRICING.get(key)
    if price is None:
        if model not in _warned_models:
            _warned_models.add(model)
            logger.warning("단가 미등록 모델 '%s' - 비용 0으로 기록. PRICING에 추가 필요.", model)
        return Decimal(0)
    cost = (
        Decimal(input_tokens) * Decimal(str(price["input"]))
        + Decimal(output_tokens) * Decimal(str(price["output"]))
    ) / _PER_MILLION
    return cost.quantize(Decimal("0.000001"))


def count_tokens(text: str, model: str) -> int:
    """tiktoken으로 텍스트의 토큰 수 계산(임베딩 등 usage를 안 주는 호출용)."""
    import tiktoken
    try:
        enc = tiktoken.encoding_for_model(_normalize_model(model))
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text or ""))


def _to_uuid(value: Union[str, uuid.UUID, None]) -> Optional[uuid.UUID]:
    if value is None or isinstance(value, uuid.UUID):
        return value
    try:
        return uuid.UUID(str(value))
    except (ValueError, AttributeError):
        return None


def record_usage(
    user_id: str,
    model: str,
    input_tokens: int,
    output_tokens: int,
    kind: str,
    conversation_id: Union[str, uuid.UUID, None] = None,
) -> None:
    """토큰 사용량 1건을 자체 DB 세션으로 적재. 실패는 삼키고 본 응답 흐름을 막지 않는다."""
    if not user_id:
        return

    from app.db import database as dbm
    from app.db.models import TokenUsage

    if dbm._session_factory is None:
        logger.error("세션 팩토리 미초기화 - 토큰 사용량 기록 스킵")
        return

    total = (input_tokens or 0) + (output_tokens or 0)
    if total == 0:
        return

    cost = compute_cost(model, input_tokens or 0, output_tokens or 0)
    with dbm._session_factory() as session:
        try:
            session.add(TokenUsage(
                user_id=str(user_id),
                conversation_id=_to_uuid(conversation_id),
                model=model,
                kind=kind,
                input_tokens=input_tokens or 0,
                output_tokens=output_tokens or 0,
                total_tokens=total,
                cost_usd=cost,
            ))
            session.commit()
        except Exception as e:  # noqa: BLE001
            session.rollback()
            logger.error("토큰 사용량 기록 실패 (user=%s, kind=%s): %s", user_id, kind, e)


def _extract_usage(response) -> dict[str, list[int]]:
    """LLMResult에서 모델별 (input, output) 토큰 집계.

    스트리밍(stream_usage=True)·비스트리밍 모두 generations의 usage_metadata를 우선 사용하고,
    없으면 llm_output.token_usage로 폴백한다.
    """
    default_model = get_settings().openai_model
    agg: dict[str, list[int]] = {}

    def add(model: str, in_tok: int, out_tok: int):
        if not (in_tok or out_tok):
            return
        slot = agg.setdefault(model, [0, 0])
        slot[0] += in_tok
        slot[1] += out_tok

    llm_output = getattr(response, "llm_output", None) or {}
    model_name = llm_output.get("model_name") or default_model

    found = False
    for gen_list in getattr(response, "generations", []) or []:
        for gen in gen_list:
            msg = getattr(gen, "message", None)
            um = getattr(msg, "usage_metadata", None) if msg is not None else None
            if um:
                add(model_name, um.get("input_tokens", 0) or 0, um.get("output_tokens", 0) or 0)
                found = True

    if not found:
        tu = llm_output.get("token_usage") or {}
        add(model_name, tu.get("prompt_tokens", 0) or 0, tu.get("completion_tokens", 0) or 0)

    return agg


class UsageCollector(BaseCallbackHandler):
    """그래프 실행 중 발생하는 모든 chat LLM 호출의 토큰을 모델별로 누적.

    한 요청당 인스턴스 1개를 만들어 graph config의 callbacks로 넘기고,
    실행 종료 후 flush(user_id, conversation_id)로 일괄 기록한다.
    """

    def __init__(self) -> None:
        self._totals: dict[str, list[int]] = {}  # model -> [input, output]

    def on_llm_end(self, response, **kwargs) -> None:  # noqa: D401
        try:
            for model, (in_tok, out_tok) in _extract_usage(response).items():
                slot = self._totals.setdefault(model, [0, 0])
                slot[0] += in_tok
                slot[1] += out_tok
        except Exception as e:  # noqa: BLE001
            logger.warning("토큰 usage 추출 실패: %s", e)

    def flush(
        self,
        user_id: str,
        conversation_id: Union[str, uuid.UUID, None] = None,
        kind: str = "chat",
    ) -> None:
        if not user_id:
            self._totals.clear()
            return
        for model, (in_tok, out_tok) in self._totals.items():
            record_usage(user_id, model, in_tok, out_tok, kind, conversation_id)
        self._totals.clear()
