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
    workflow.add_edge("code_generation", "agent")
    workflow.add_edge("rag_search", "agent")
    workflow.add_edge("agent", END)

    return workflow.compile()


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
            "code": code,
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


def run_agent(question: str, source_code: Optional[str] = None, file_name: Optional[str] = None, error_info: Optional[str] = None, history: Optional[List[dict]] = None) -> Dict[str, Any]:
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    full_question = _build_full_question(question, source_code, file_name, error_info)
    history_messages = _build_history_messages(history)

    result = _graph.invoke({
        "messages": history_messages + [HumanMessage(content=full_question)],
        "intent": None,
        "context": None,
    })

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


async def run_agent_stream(question: str, source_code: Optional[str] = None, file_name: Optional[str] = None, error_info: Optional[str] = None, history: Optional[List[dict]] = None):
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    full_question = _build_full_question(question, source_code, file_name, error_info)
    history_messages = _build_history_messages(history)
    collected_content = []

    async for event in _graph.astream_events(
        {
            "messages": history_messages + [HumanMessage(content=full_question)],
            "intent": None,
            "context": None,
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
