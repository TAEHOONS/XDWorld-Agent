"""LangGraph 기반 RAG Agent 파이프라인.

Intent Router를 통해 요청 유형을 분류하고,
각 전문 노드로 라우팅하는 구조입니다.

흐름:
  START → intent_router → error_analysis  ↘
                        → code_generation  → agent → END
                        → rag_search      ↗
"""

from __future__ import annotations

import json
import re
from typing import Annotated, Any, Dict, List, Literal, Optional, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

from app.core.config import get_settings
from app.core.exceptions import LLMError
from app.core.logging import logger
from app.services.vectorstore import get_retriever
from app.services.prompts import AGENT_SYSTEM_PROMPT


# ── State ──────────────────────────────────────────────

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    intent: Optional[str]          # "error_analysis" | "code_generation" | "rag_search"
    context: Optional[str]         # 검색/분석 결과 컨텍스트


# ── Tools ──────────────────────────────────────────────

@tool
def search_manual(query: str) -> str:
    """XDWorld 지도 엔진 메뉴얼에서 관련 문서를 검색합니다."""
    logger.info("도구 호출 - search_manual: %s", query[:80])
    
    from app.services.retrieval import search_with_enhancement
    
    docs = search_with_enhancement(query)
    if not docs:
        return "검색 결과가 없습니다."
    
    results = []
    for doc in docs:
        source = doc.metadata.get("relative_path", "unknown")
        results.append(f"[출처: {source}]\n{doc.page_content}")
    
    return "\n\n---\n\n".join(results)


TOOLS = [search_manual]


def _get_llm(temperature: Optional[float] = None):
    settings = get_settings()
    return ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
        temperature=temperature if temperature is not None else settings.openai_temperature,
    )


# ── Node 1: Intent Router ──────────────────────────────

from app.services.intent_classifier import classify_by_keywords as _classify_by_keywords  # noqa: E402


def intent_router_node(state: AgentState) -> AgentState:
    """사용자 요청 의도를 분류. 키워드로 1차 분류 후 애매하면 LLM 폴백."""
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"intent": "rag_search", "context": None}

    content = last_human.content
    has_source_code = "```" in content
    has_error_info = bool(re.search(r"에러\s*정보\s*:", content))

    # 1차: 키워드 분류 (LLM 호출 없음)
    fast = _classify_by_keywords(content, has_source_code, has_error_info)
    if fast:
        logger.info("Intent 분류(keyword): %s (질문: %s)", fast, content[:100])
        return {"intent": fast, "context": None}

    # 2차: LLM 폴백
    llm = _get_llm(temperature=0)
    prompt = f"""다음 사용자 요청을 분석하여 의도를 분류하세요.

사용자 요청: {content}

분류 기준:
- error_analysis: 에러 분석/디버깅 요청
  예: "이 에러가 왜 나요?", "오류 해결 방법", "디버깅 도와줘"

- code_generation: 코드 예제/샘플이 필요한 모든 요청
  예: "카메라 이동 방법 알려줘", "마커 추가하는 법", "지도 생성 어떻게 해?",
      "레이어 사용법", "코드 만들어줘", "예제 보여줘", "구현 방법"

- rag_search: 개념/용어 설명, 단순 정보 조회
  예: "XDWorld가 뭐야?", "레이어란?", "좌표계 종류", "지원하는 포맷"

반드시 다음 중 하나만 응답: error_analysis, code_generation, rag_search"""

    response = llm.invoke([HumanMessage(content=prompt)])
    intent = response.content.strip().lower()

    if intent not in ["error_analysis", "code_generation", "rag_search"]:
        intent = "rag_search"

    logger.info("Intent 분류(LLM): %s (질문: %s)", intent, content[:100])
    return {"intent": intent, "context": None}


# ── Node 2: Error Analysis ─────────────────────────────

def error_analysis_node(state: AgentState) -> AgentState:
    """에러를 분석하고 원인과 해결책을 찾는 노드."""
    from app.services.retrieval import search_with_enhancement
    
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"context": ""}

    # 에러 관련 키워드로 매뉴얼 검색
    content = last_human.content
    error_lines = [l for l in content.split("\n") if "error" in l.lower() or "에러" in l]
    query = " ".join(error_lines[:3]) if error_lines else content[:200]

    docs = search_with_enhancement(f"에러 해결 {query}")
    
    context_parts = ["[에러 분석을 위한 관련 문서]"]
    for doc in docs:
        source = doc.metadata.get("relative_path", "unknown")
        context_parts.append(f"[출처: {source}]\n{doc.page_content}")
    
    context = "\n\n---\n\n".join(context_parts)
    logger.info("에러 분석 컨텍스트 수집 완료 (%d개 문서)", len(docs))
    return {"context": context}


# ── Node 3: Code Generation ────────────────────────────

def code_generation_node(state: AgentState) -> AgentState:
    """코드 생성에 필요한 API 문서를 검색하는 노드."""
    from app.services.retrieval import search_with_enhancement

    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"context": ""}

    # 코드 블록 제거 후 순수 질문만 검색 쿼리로 사용
    # (source_code의 함수명이 검색 쿼리를 오염시키는 것을 방지)
    clean_content = re.sub(r"```[\s\S]*?```", "", last_human.content).strip()
    query = clean_content[:300]

    docs = search_with_enhancement(query)

    context_parts = ["[코드 생성을 위한 API 문서 및 예제]"]
    for doc in docs:
        source = doc.metadata.get("relative_path", "unknown")
        context_parts.append(f"[출처: {source}]\n{doc.page_content}")

    context = "\n\n---\n\n".join(context_parts)
    logger.info("코드 생성 컨텍스트 수집 완료 (%d개 문서)", len(docs))
    return {"context": context}


# ── Node 4: RAG Search ─────────────────────────────────

def rag_search_node(state: AgentState) -> AgentState:
    """일반 질문에 대한 RAG 검색 노드."""
    from app.services.retrieval import search_with_enhancement

    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"context": ""}

    # 코드 블록 제거 후 순수 질문만 검색 쿼리로 사용
    # (source_code의 함수명이 검색 쿼리를 오염시키는 것을 방지)
    clean_content = re.sub(r"```[\s\S]*?```", "", last_human.content).strip()
    query = clean_content[:300]

    docs = search_with_enhancement(query)

    context_parts = ["[관련 문서]"]
    for doc in docs:
        source = doc.metadata.get("relative_path", "unknown")
        context_parts.append(f"[출처: {source}]\n{doc.page_content}")

    context = "\n\n---\n\n".join(context_parts)
    logger.info("RAG 검색 완료 (%d개 문서)", len(docs))
    return {"context": context}


# ── Node 5: Agent (최종 답변) ──────────────────────────

def agent_node(state: AgentState) -> AgentState:
    """검색/분석 결과를 바탕으로 최종 답변을 생성하는 노드."""
    intent = state.get("intent", "rag_search")
    context = state.get("context", "")

    # intent별 시스템 프롬프트 커스터마이징
    intent_instructions = {
        "error_analysis": "사용자의 에러를 분석하고, 원인과 해결 방법을 단계별로 설명하세요. 수정된 코드가 필요하면 code_suggestions에 포함하세요.",
        "code_generation": "사용자가 요청한 기능에 필요한 최소 코드 스니펫만 생성하세요. 전체 SFC(<template>/<script>/<style>) 재작성은 사용자가 명시적으로 전체 파일을 요청한 경우에만 하세요. 반드시 code_suggestions 형식으로 코드를 제공하세요.",
        "rag_search": "검색된 문서를 바탕으로 질문에 정확하게 답변하세요.",
    }

    system_content = f"{AGENT_SYSTEM_PROMPT}\n\n## 현재 작업\n{intent_instructions.get(intent, '')}"
    if context:
        system_content += f"\n\n{context}"

    # state.messages는 add_messages 누적 reducer라서 같은 thread_id 재사용 시
    # 이전 turn의 HumanMessage가 그대로 쌓임. 오염 방지를 위해 가장 최근 1개만 사용.
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    messages = [SystemMessage(content=system_content)]
    if last_human:
        messages.append(last_human)

    llm = _get_llm()
    try:
        response = llm.invoke(messages)
    except Exception as exc:
        logger.error("LLM 호출 실패: %s", exc)
        raise LLMError(f"LLM 호출 중 오류 발생: {exc}") from exc

    logger.info("최종 답변 생성 완료 (intent: %s)", intent)
    return {"messages": [response]}


# ── Routing Functions ──────────────────────────────────

def route_by_intent(state: AgentState) -> str:
    """intent에 따라 전문 노드로 라우팅."""
    return state.get("intent", "rag_search")


# ── Graph ──────────────────────────────────────────────

def _get_db_url():
    from app.db.database import get_sync_db_url
    return get_sync_db_url()


def _get_checkpointer():
    """동기 PostgreSQL checkpointer 생성"""
    import psycopg
    conn = psycopg.connect(_get_db_url(), autocommit=True, prepare_threshold=0)
    return PostgresSaver(conn)


async def _get_async_checkpointer():
    """비동기 PostgreSQL checkpointer 생성"""
    import psycopg
    conn = await psycopg.AsyncConnection.connect(_get_db_url(), autocommit=True, prepare_threshold=0)
    return AsyncPostgresSaver(conn)


def _build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("intent_router", intent_router_node)
    workflow.add_node("error_analysis", error_analysis_node)
    workflow.add_node("code_generation", code_generation_node)
    workflow.add_node("rag_search", rag_search_node)
    workflow.add_node("agent", agent_node)

    workflow.set_entry_point("intent_router")

    # intent_router → 각 전문 노드
    workflow.add_conditional_edges(
        "intent_router",
        route_by_intent,
        {
            "error_analysis": "error_analysis",
            "code_generation": "code_generation",
            "rag_search": "rag_search",
        },
    )

    # 각 전문 노드 → agent (최종 답변)
    workflow.add_edge("error_analysis", "agent")
    workflow.add_edge("rag_search", "agent")
    workflow.add_edge("code_generation", "agent")
    workflow.add_edge("agent", END)

    # Checkpointer 설정 + agent 전 중단
    checkpointer = _get_checkpointer()
    checkpointer.setup()  # 테이블 생성
    return workflow.compile(checkpointer=checkpointer, interrupt_before=["agent"])


async def _build_graph_streaming():
    """스트리밍용 그래프 (AsyncPostgresSaver 사용). agent 노드 전 중단."""
    workflow = StateGraph(AgentState)

    workflow.add_node("intent_router", intent_router_node)
    workflow.add_node("error_analysis", error_analysis_node)
    workflow.add_node("code_generation", code_generation_node)
    workflow.add_node("rag_search", rag_search_node)
    workflow.add_node("agent", agent_node)

    workflow.set_entry_point("intent_router")

    workflow.add_conditional_edges(
        "intent_router",
        route_by_intent,
        {
            "error_analysis": "error_analysis",
            "code_generation": "code_generation",
            "rag_search": "rag_search",
        },
    )

    workflow.add_edge("error_analysis", "agent")
    workflow.add_edge("code_generation", "agent")
    workflow.add_edge("rag_search", "agent")
    workflow.add_edge("agent", END)

    checkpointer = await _get_async_checkpointer()
    await checkpointer.setup()
    # interrupt_before로 agent 실행 직전 자동 중단 → 코드 생성에서 HITL 가능
    return workflow.compile(checkpointer=checkpointer, interrupt_before=["agent"])


_graph = _build_graph()
_graph_streaming = None  # main.py lifespan에서 초기화


# ── Response Parser ────────────────────────────────────
# 파싱 로직은 app/services/response_parser.py로 분리되었습니다.
from app.services.response_parser import parse_response as _parse_response  # noqa: E402


# ── Public API ─────────────────────────────────────────

def _build_full_question(question: str, source_code: Optional[str], file_name: Optional[str], error_info: Optional[str]) -> str:
    parts = [question.strip()]
    if source_code:
        parts.append(f"\n\n현재 코드 ({file_name or 'unknown'}):\n```{file_name.split('.')[-1] if file_name else 'vue'}\n{source_code}\n```")
    if error_info:
        parts.append(f"\n\n에러 정보:\n{error_info}")
    return "\n".join(parts)


def _build_history_messages(history: Optional[List[dict]]) -> List[BaseMessage]:
    """이전 대화 히스토리를 LangChain 메시지로 변환 (최근 10개만)"""
    if not history:
        return []
    messages = []
    for h in history[-10:]:
        role = h.get("role", "")
        content = h.get("content", "")
        if not content:
            continue
        if role == "user":
            messages.append(HumanMessage(content=content))
        elif role in ("agent", "assistant"):
            messages.append(AIMessage(content=content))
    return messages


def run_agent(
    question: str, 
    source_code: Optional[str] = None, 
    file_name: Optional[str] = None, 
    error_info: Optional[str] = None, 
    history: Optional[List[dict]] = None,
    thread_id: Optional[str] = None,
    db: Optional[Any] = None,
    user_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Agent 실행. thread_id가 있으면 중단된 상태에서 재개.
    
    Returns:
        - 정상 완료: {"answer": ..., "code_suggestions": ...}
        - 중단됨: {"interrupted": True, "thread_id": ..., "context": ..., "next_node": "agent"}
    """
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    full_question = _build_full_question(question, source_code, file_name, error_info)
    history_messages = _build_history_messages(history)
    
    # 유사 대화 검색 및 컨텍스트 추가
    similar_context = ""
    if db and user_id:
        from app.services.conversation import search_similar_conversations
        similar = search_similar_conversations(question, user_id, db, limit=3)
        if similar:
            similar_parts = ["[과거 유사 대화 참고]"]
            for s in similar:
                similar_parts.append(f"- {s['role']}: {s['summary']} (유사도: {s['similarity']:.2f})")
            similar_context = "\n".join(similar_parts)
            logger.info("유사 대화 %d개 추가", len(similar))
    
    # thread_id 생성 (없으면 새로 생성)
    import uuid
    if not thread_id:
        thread_id = str(uuid.uuid4())
    
    config = {"configurable": {"thread_id": thread_id}}

    result = _graph.invoke({
        "messages": history_messages + [HumanMessage(content=full_question)],
        "intent": None,
        "context": similar_context,
    }, config=config)
    
    # 중단 여부 확인
    state = _graph.get_state(config)
    intent = state.values.get("intent", "")
    
    # code_generation일 때만 중단 상태 반환
    if intent == "code_generation" and state.next:
        return {
            "interrupted": True,
            "thread_id": thread_id,
            "context": state.values.get("context", ""),
            "intent": intent,
            "message": "검색된 API 문서를 확인하고 코드 생성을 승인해주세요."
        }
    
    # error_analysis, rag_search는 중단 무시하고 바로 재개
    if state.next and intent != "code_generation":
        result = _graph.invoke(None, config=config)
    
    # 정상 완료
    for msg in reversed(result["messages"]):
        if isinstance(msg, AIMessage) and msg.content:
            return _parse_response(msg.content)

    return {"answer": "답변을 생성하지 못했습니다.", "code_suggestions": None}


async def resume_agent_stream(
    thread_id: str,
    approved: bool = True,
    additional_context: Optional[str] = None
):
    """중단된 Agent를 SSE로 재개. step/token/code_pending/result 이벤트 yield."""
    global _graph_streaming
    if _graph_streaming is None:
        _graph_streaming = await _build_graph_streaming()

    config = {"configurable": {"thread_id": thread_id}}

    state = await _graph_streaming.aget_state(config)
    if not state.next:
        raise ValueError("재개할 중단 상태가 없습니다.")

    if not approved:
        yield {"type": "result", "answer": "사용자가 코드 생성을 취소했습니다.", "code_suggestions": None}
        return

    if additional_context:
        current_context = state.values.get("context", "")
        updated_context = f"{current_context}\n\n[사용자 추가 요청]\n{additional_context}"
        await _graph_streaming.aupdate_state(config, {"context": updated_context})

    collected_content: List[str] = []
    async for evt in _stream_graph_events(None, config, collected_content):
        yield evt

    full_content = "".join(collected_content)
    if full_content:
        parsed = _parse_response(full_content)
        yield {"type": "result", "answer": parsed["answer"], "code_suggestions": parsed.get("code_suggestions")}
    else:
        yield {"type": "result", "answer": "답변을 생성하지 못했습니다.", "code_suggestions": None}


def resume_agent(thread_id: str, approved: bool = True, additional_context: Optional[str] = None) -> Dict[str, Any]:
    """
    중단된 Agent 재개.

    Args:
        thread_id: 중단된 스레드 ID
        approved: 사용자 승인 여부
        additional_context: 추가 컨텍스트 (사용자가 수정/추가한 내용)

    Returns:
        {"answer": ..., "code_suggestions": ...}
    """
    config = {"configurable": {"thread_id": thread_id}}
    
    # 현재 상태 조회
    state = _graph.get_state(config)
    if not state.next:
        raise ValueError("재개할 중단 상태가 없습니다.")
    
    # 사용자가 거부하면 중단
    if not approved:
        return {"answer": "사용자가 코드 생성을 취소했습니다.", "code_suggestions": None}
    
    # 추가 컨텍스트가 있으면 상태 업데이트
    if additional_context:
        current_context = state.values.get("context", "")
        updated_context = f"{current_context}\n\n[사용자 추가 요청]\n{additional_context}"
        _graph.update_state(config, {"context": updated_context})
    
    # 재개
    result = _graph.invoke(None, config=config)
    
    # 응답 파싱
    for msg in reversed(result["messages"]):
        if isinstance(msg, AIMessage) and msg.content:
            return _parse_response(msg.content)
    
    return {"answer": "답변을 생성하지 못했습니다.", "code_suggestions": None}


# intent → 프론트 step 매핑
_INTENT_STEPS = {
    "error_analysis":  ("analyzing", "에러 분석 중..."),
    "code_generation": ("analyzing", "요청 분석 중..."),
    "rag_search":      ("analyzing", "질문 분석 중..."),
}
_NODE_STEPS = {
    "error_analysis":  ("searching",  "에러 원인 검색 중..."),
    "code_generation": ("searching",  "API 문서 검색 중..."),
    "rag_search":      ("searching",  "관련 문서 검색 중..."),
    "agent":           ("generating", "답변 생성 중..."),
}


_CODE_MARKER = "```json:code_suggestions"
_CODE_MARKER_HOLD = len(_CODE_MARKER) - 1  # 마커가 토큰 경계에 걸쳐 분할되는 경우 대비 버퍼


async def _stream_graph_events(input_data, config, collected_content):
    """그래프 이벤트를 스트리밍하며 토큰을 수집. step/intent/token/code_pending 이벤트 yield."""
    in_suppress = False  # code_suggestions JSON 블록 진입 후 토큰 송출 중단
    pending = ""         # 마커 감지를 위한 슬라이딩 버퍼

    async for event in _graph_streaming.astream_events(
        input_data, config=config, version="v1"
    ):
        kind = event["event"]
        name = event.get("name", "")

        if kind == "on_chain_start" and name in _NODE_STEPS:
            step, message = _NODE_STEPS[name]
            yield {"type": "step", "step": step, "message": message}

        elif kind == "on_chain_end" and name == "intent_router":
            output = event.get("data", {}).get("output", {})
            intent = output.get("intent", "rag_search")
            _, message = _INTENT_STEPS.get(intent, ("analyzing", "분석 중..."))
            yield {"type": "step", "step": "analyzing", "message": message, "intent": intent}

        elif kind == "on_chat_model_stream":
            # agent 노드의 토큰만 클라이언트로 송출
            # (intent_router, expand_query, rerank 등 내부 LLM 호출의 토큰은 무시)
            if event.get("metadata", {}).get("langgraph_node") != "agent":
                continue
            chunk = event["data"]["chunk"]
            if not (hasattr(chunk, "content") and chunk.content):
                continue

            content = chunk.content
            collected_content.append(content)  # 최종 파싱용으로 항상 수집

            if in_suppress:
                continue  # 마커 이후 JSON 블록은 클라이언트로 송출하지 않음

            pending += content

            # 마커 발견 → 그 이전까지만 emit 후 code_pending 신호
            if _CODE_MARKER in pending:
                pos = pending.index(_CODE_MARKER)
                if pos > 0:
                    yield {"type": "token", "content": pending[:pos]}
                pending = ""
                in_suppress = True
                yield {"type": "code_pending"}
                continue

            # 마커가 토큰 경계로 잘려 있을 수 있으니, 마지막 (HOLD)자만 보류하고 나머지 emit
            if len(pending) > _CODE_MARKER_HOLD:
                safe = pending[:-_CODE_MARKER_HOLD]
                pending = pending[-_CODE_MARKER_HOLD:]
                if safe:
                    yield {"type": "token", "content": safe}

    # 스트림 종료 시 보류분 플러시 (마커가 없었던 경우)
    if pending and not in_suppress:
        yield {"type": "token", "content": pending}


async def run_agent_stream(
    question: str,
    source_code: Optional[str] = None,
    file_name: Optional[str] = None,
    error_info: Optional[str] = None,
    history: Optional[List[dict]] = None,
    thread_id: Optional[str] = None,
    db: Optional[Any] = None,
    user_id: Optional[str] = None
):
    global _graph_streaming
    if _graph_streaming is None:
        _graph_streaming = await _build_graph_streaming()
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    full_question = _build_full_question(question, source_code, file_name, error_info)
    history_messages = _build_history_messages(history)

    # 유사 대화 검색 및 컨텍스트 추가
    similar_context = ""
    if db and user_id:
        from app.services.conversation import search_similar_conversations
        similar = search_similar_conversations(question, user_id, db, limit=3)
        if similar:
            similar_parts = ["[과거 유사 대화 참고]"]
            for s in similar:
                similar_parts.append(f"- {s['role']}: {s['summary']} (유사도: {s['similarity']:.2f})")
            similar_context = "\n".join(similar_parts)
            logger.info("유사 대화 %d개 추가", len(similar))

    # thread_id 생성
    import uuid
    if not thread_id:
        thread_id = str(uuid.uuid4())

    config = {"configurable": {"thread_id": thread_id}}
    collected_content: List[str] = []

    # Phase 1: 검색 노드까지 실행 (interrupt_before=["agent"]로 자동 중단)
    initial_input = {
        "messages": history_messages + [HumanMessage(content=full_question)],
        "intent": None,
        "context": similar_context,
    }
    async for evt in _stream_graph_events(initial_input, config, collected_content):
        yield evt

    # 중단 지점 상태 확인
    state = await _graph_streaming.aget_state(config)
    intent = state.values.get("intent", "rag_search")

    # code_generation은 HITL 중단 (사용자 승인 후 /resume으로 재개)
    if state.next and intent == "code_generation":
        yield {
            "type": "interrupted",
            "thread_id": thread_id,
            "context": state.values.get("context", ""),
            "intent": intent,
            "message": "검색된 API 문서를 확인하고 코드 생성을 승인해주세요."
        }
        return

    # error_analysis, rag_search는 그대로 agent 실행 (None으로 resume → agent 토큰 스트림)
    if state.next:
        async for evt in _stream_graph_events(None, config, collected_content):
            yield evt

    # 최종 답변
    full_content = "".join(collected_content)
    if full_content:
        parsed = _parse_response(full_content)
        yield {"type": "result", "answer": parsed["answer"], "code_suggestions": parsed.get("code_suggestions")}
    else:
        yield {"type": "result", "answer": "답변을 생성하지 못했습니다.", "code_suggestions": None}


if __name__ == "__main__":
    result = run_agent("레이어 추가 방법은?")
    print("answer:", result["answer"])
    if result.get("code_suggestions"):
        print("code_suggestions:", json.dumps(result["code_suggestions"], ensure_ascii=False, indent=2))
