"""LangGraph 기반 RAG Agent 파이프라인.

LLM이 검색 도구 호출 여부를 스스로 판단하고,
필요하면 재검색하는 Agent 구조입니다.
"""

from __future__ import annotations

from typing import Annotated, List, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
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


# ── Tool ───────────────────────────────────────────────

@tool
def search_manual(query: str) -> str:
    """XDWorld 지도 엔진 메뉴얼에서 관련 문서를 검색합니다.
    질문과 관련된 API 문서, 튜토리얼, 예제 코드를 찾을 때 사용하세요."""
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


# ── Nodes ──────────────────────────────────────────────

def agent_node(state: AgentState) -> AgentState:
    """LLM이 도구 호출 여부를 판단하는 노드."""
    settings = get_settings()
    llm = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
        temperature=settings.openai_temperature,
    ).bind_tools(TOOLS)

    try:
        response = llm.invoke(state["messages"])
    except Exception as exc:
        logger.error("LLM 호출 실패: %s", exc)
        raise LLMError(f"LLM 호출 중 오류 발생: {exc}") from exc

    logger.info(
        "Agent 응답 - tool_calls: %d개",
        len(response.tool_calls) if hasattr(response, "tool_calls") else 0,
    )
    return {"messages": [response]}


def tool_node(state: AgentState) -> AgentState:
    """Agent가 요청한 도구를 실행하는 노드."""
    last_message: AIMessage = state["messages"][-1]
    tool_map = {t.name: t for t in TOOLS}
    results = []

    for call in last_message.tool_calls:
        tool_name = call["name"]
        tool_args = call["args"]
        logger.info("도구 실행: %s(%s)", tool_name, tool_args)

        if tool_name in tool_map:
            result = tool_map[tool_name].invoke(tool_args)
        else:
            result = f"알 수 없는 도구: {tool_name}"

        results.append(
            ToolMessage(content=str(result), tool_call_id=call["id"])
        )

    return {"messages": results}


# ── Routing ────────────────────────────────────────────

def should_continue(state: AgentState) -> str:
    """마지막 메시지에 tool_calls가 있으면 도구 실행, 없으면 종료."""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"


# ── Graph ──────────────────────────────────────────────

def _build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {"tools": "tools", "end": END},
    )
    workflow.add_edge("tools", "agent")

    return workflow.compile()


_graph = _build_graph()


def run_agent(question: str) -> str:
    """질문을 받아 Agent 파이프라인을 실행하고 답변을 반환합니다."""
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    initial_messages = [
        {"role": "system", "content": AGENT_SYSTEM_PROMPT},
        HumanMessage(content=question.strip()),
    ]

    result = _graph.invoke({"messages": initial_messages})

    # 마지막 AI 메시지에서 답변 추출
    for msg in reversed(result["messages"]):
        if isinstance(msg, AIMessage) and msg.content:
            logger.info("최종 답변 생성 완료 (%d자)", len(msg.content))
            return msg.content

    return "답변을 생성하지 못했습니다."


if __name__ == "__main__":
    answer = run_agent("레이어 추가 방법은?")
    print("\n===== 최종 답변 =====\n")
    print(answer)
