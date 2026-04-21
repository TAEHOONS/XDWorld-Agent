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
    retriever = get_retriever()
    docs = retriever.invoke(query)
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

def intent_router_node(state: AgentState) -> AgentState:
    """사용자 요청 의도를 분류하는 노드."""
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"intent": "rag_search", "context": None}

    content = last_human.content

    # 에러 정보가 포함된 경우
    if "에러 정보:" in content or "Error" in content or "에러" in content and "코드:" in content:
        intent = "error_analysis"
    # 코드 생성/수정 요청
    elif any(kw in content for kw in ["만들어", "작성해", "생성해", "수정해", "추가해", "구현해", "코드로"]):
        intent = "code_generation"
    # 일반 질문
    else:
        intent = "rag_search"

    logger.info("Intent 분류: %s", intent)
    return {"intent": intent, "context": None}


    logger.info("Intent 분류: %s", intent)
    return {"intent": intent, "context": None}


# ── Node 2: Error Analysis ─────────────────────────────

def error_analysis_node(state: AgentState) -> AgentState:
    """에러를 분석하고 원인과 해결책을 찾는 노드."""
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"context": ""}

    # 에러 관련 키워드로 매뉴얼 검색
    content = last_human.content
    error_lines = [l for l in content.split("\n") if "error" in l.lower() or "에러" in l]
    query = " ".join(error_lines[:3]) if error_lines else content[:200]

    retriever = get_retriever()
    docs = retriever.invoke(f"에러 해결 {query}")
    
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
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"context": ""}

    content = last_human.content
    # 코드 블록 제거하고 핵심 요청만 추출
    clean_content = re.sub(r"```[\s\S]*?```", "", content).strip()
    query = clean_content[:300]

    retriever = get_retriever()
    # 코드 예제 위주로 검색
    docs = retriever.invoke(f"코드 예제 {query}")
    
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
    last_human = next(
        (m for m in reversed(state["messages"]) if isinstance(m, HumanMessage)), None
    )
    if not last_human:
        return {"context": ""}

    content = last_human.content
    clean_content = re.sub(r"```[\s\S]*?```", "", content).strip()
    query = clean_content[:300]

    retriever = get_retriever()
    docs = retriever.invoke(query)
    
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
        "code_generation": "사용자가 요청한 기능을 구현하는 완전한 Vue 코드를 생성하세요. 반드시 code_suggestions 형식으로 코드를 제공하세요.",
        "rag_search": "검색된 문서를 바탕으로 질문에 정확하게 답변하세요.",
    }

    system_content = f"{AGENT_SYSTEM_PROMPT}\n\n## 현재 작업\n{intent_instructions.get(intent, '')}"
    if context:
        system_content += f"\n\n{context}"

    # 기존 메시지에서 HumanMessage만 추출 (system 메시지 교체)
    human_messages = [m for m in state["messages"] if isinstance(m, HumanMessage)]
    
    messages = [SystemMessage(content=system_content)] + human_messages

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

def _get_checkpointer():
    """PostgreSQL checkpointer 생성"""
    settings = get_settings()
    # psycopg URL로 변환
    db_url = settings.database_url.replace("postgresql+asyncpg://", "postgresql://").replace("postgresql+psycopg2://", "postgresql://")
    
    # PostgresSaver 직접 생성
    import psycopg
    conn = psycopg.connect(db_url, autocommit=True, prepare_threshold=0)
    return PostgresSaver(conn)


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


_graph = _build_graph()


# ── Response Parser ────────────────────────────────────

_EXPLICIT_PATTERN = re.compile(
    r"```json:code_suggestions\s*\n(.*?)\n```",
    re.DOTALL,
)
_MD_CODE_BLOCK_PATTERN = re.compile(
    r"^[ \t]*```(\w+)?\s*\n(.*?)\n[ \t]*```",
    re.DOTALL | re.MULTILINE,
)
_LANG_MAP = {
    "javascript": "js", "js": "js", "typescript": "ts", "ts": "ts",
    "vue": "vue", "html": "html", "css": "css", "python": "python",
    "py": "python", "json": "json", "bash": "bash", "sh": "bash",
}


def _strip_initialize_wrapper(code: str) -> str:
    """initialize() 함수로 감싸진 코드에서 내부 코드만 추출."""
    match = re.match(
        r'^\s*function\s+initialize\s*\(\s*\)\s*\{([\s\S]*)\}\s*$',
        code.strip()
    )
    if not match:
        return code
    inner = match.group(1).strip()
    lines = inner.split('\n')
    dedented = '\n'.join(l[2:] if l.startswith('  ') else l for l in lines)
    return dedented.strip()


def _parse_response(content: str) -> Dict[str, Any]:
    explicit = _EXPLICIT_PATTERN.search(content)
    if explicit:
        answer = content[: explicit.start()].strip()
        trailing = content[explicit.end() :].strip()
        if trailing:
            answer = f"{answer}\n\n{trailing}" if answer else trailing
        try:
            suggestions = json.loads(explicit.group(1))
            if not isinstance(suggestions, list):
                suggestions = [suggestions]
            for s in suggestions:
                if isinstance(s.get("code"), str):
                    s["code"] = _strip_initialize_wrapper(s["code"])
            return {"answer": answer, "code_suggestions": suggestions or None}
        except (json.JSONDecodeError, TypeError):
            logger.warning("code_suggestions JSON 파싱 실패, 폴백으로 코드블록 추출")

    blocks = list(_MD_CODE_BLOCK_PATTERN.finditer(content))
    if not blocks:
        return {"answer": content.strip(), "code_suggestions": None}

    suggestions = []
    answer = content
    for match in reversed(blocks):
        lang_hint = (match.group(1) or "").lower()
        code = match.group(2).strip()
        if not code:
            continue
        language = _LANG_MAP.get(lang_hint, lang_hint or "js")
        suggestions.append({
            "filename": f"example.{language}" if language else "example.js",
            "language": language or "js",
            "code": _strip_initialize_wrapper(code),
        })
        answer = answer[: match.start()].rstrip() + answer[match.end() :].lstrip()

    suggestions.reverse()
    return {"answer": answer.strip(), "code_suggestions": suggestions if suggestions else None}


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
    db: Optional[Any] = None
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
    if db:
        from app.services.conversation import search_similar_conversations
        similar = search_similar_conversations(question, db, limit=3)
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
    intent = result.get("intent", "")
    
    # code_generation일 때만 중단 상태 반환
    if intent == "code_generation" and state.next:
        return {
            "interrupted": True,
            "thread_id": thread_id,
            "context": result.get("context", ""),
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


async def run_agent_stream(
    question: str, 
    source_code: Optional[str] = None, 
    file_name: Optional[str] = None, 
    error_info: Optional[str] = None, 
    history: Optional[List[dict]] = None,
    db: Optional[Any] = None
):
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    full_question = _build_full_question(question, source_code, file_name, error_info)
    history_messages = _build_history_messages(history)
    
    # 유사 대화 검색 및 컨텍스트 추가
    similar_context = ""
    if db:
        from app.services.conversation import search_similar_conversations
        similar = search_similar_conversations(question, db, limit=3)
        if similar:
            similar_parts = ["[과거 유사 대화 참고]"]
            for s in similar:
                similar_parts.append(f"- {s['role']}: {s['summary']} (유사도: {s['similarity']:.2f})")
            similar_context = "\n".join(similar_parts)
            logger.info("유사 대화 %d개 추가", len(similar))
    
    collected_content = []

    async for event in _graph.astream_events(
        {
            "messages": history_messages + [HumanMessage(content=full_question)],
            "intent": None,
            "context": similar_context,
        },
        version="v1"
    ):
        kind = event["event"]
        name = event.get("name", "")

        if kind == "on_chain_start" and name in _NODE_STEPS:
            step, message = _NODE_STEPS[name]
            yield {"type": "step", "step": step, "message": message}

        elif kind == "on_chain_end" and name == "intent_router":
            # intent 결정 직후 → 어떤 노드로 갈지 알림
            output = event.get("data", {}).get("output", {})
            intent = output.get("intent", "rag_search")
            _, message = _INTENT_STEPS.get(intent, ("analyzing", "분석 중..."))
            yield {"type": "step", "step": "analyzing", "message": message, "intent": intent}

        elif kind == "on_chat_model_stream":
            chunk = event["data"]["chunk"]
            if hasattr(chunk, "content") and chunk.content:
                collected_content.append(chunk.content)
                yield {"type": "token", "content": chunk.content}

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
