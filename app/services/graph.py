"""LangGraph 기반 RAG Agent 파이프라인.

LLM이 검색 도구 호출 여부를 스스로 판단하고,
필요하면 재검색하는 Agent 구조입니다.
"""

from __future__ import annotations

import json
import re
from typing import Annotated, Any, Dict, List, Optional, TypedDict

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


# LLM이 json:code_suggestions 블록을 사용한 경우
_EXPLICIT_PATTERN = re.compile(
    r"```json:code_suggestions\s*\n(.*?)\n```",
    re.DOTALL,
)

# 일반 마크다운 코드블록: ```lang\n...\n``` (들여쓰기 포함)
_MD_CODE_BLOCK_PATTERN = re.compile(
    r"^[ \t]*```(\w+)?\s*\n(.*?)\n[ \t]*```",
    re.DOTALL | re.MULTILINE,
)

# 언어 힌트 → language 매핑
_LANG_MAP = {
    "javascript": "js", "js": "js", "typescript": "ts", "ts": "ts",
    "vue": "vue", "html": "html", "css": "css", "python": "python",
    "py": "python", "json": "json", "bash": "bash", "sh": "bash",
}


def _parse_response(content: str) -> Dict[str, Any]:
    """LLM 응답에서 answer 텍스트와 code_suggestions를 분리합니다.

    1순위: ```json:code_suggestions 블록이 있으면 그대로 파싱
    2순위: 일반 마크다운 코드블록을 자동 추출해서 code_suggestions로 변환
    """
    # ── 1순위: 명시적 json:code_suggestions 블록 ──
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

    # ── 2순위: 마크다운 코드블록 자동 추출 ──
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
        # answer에서 코드블록 제거
        answer = answer[: match.start()].rstrip() + answer[match.end() :].lstrip()

    suggestions.reverse()
    answer = answer.strip()

    return {
        "answer": answer,
        "code_suggestions": suggestions if suggestions else None,
    }


def run_agent(question: str, source_code: Optional[str] = None, file_name: Optional[str] = None, error_info: Optional[str] = None) -> Dict[str, Any]:
    """질문을 받아 Agent 파이프라인을 실행하고 answer + code_suggestions를 반환합니다."""
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    # 컨텍스트 추가
    context_parts = [question.strip()]
    if source_code:
        context_parts.append(f"\n\n현재 코드:\n```{file_name or 'vue'}\n{source_code}\n```")
    if error_info:
        context_parts.append(f"\n\n에러 정보:\n{error_info}")
    
    full_question = "\n".join(context_parts)

    initial_messages = [
        {"role": "system", "content": AGENT_SYSTEM_PROMPT},
        HumanMessage(content=full_question),
    ]

    result = _graph.invoke({"messages": initial_messages})

    # 마지막 AI 메시지에서 답변 추출
    for msg in reversed(result["messages"]):
        if isinstance(msg, AIMessage) and msg.content:
            logger.info("최종 답변 생성 완료 (%d자)", len(msg.content))
            return _parse_response(msg.content)

    return {"answer": "답변을 생성하지 못했습니다.", "code_suggestions": None}


async def run_agent_stream(question: str, source_code: Optional[str] = None, file_name: Optional[str] = None, error_info: Optional[str] = None):
    """LangGraph 실행하면서 각 노드 진행 상황을 yield"""
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    # 컨텍스트 추가
    context_parts = [question.strip()]
    if source_code:
        context_parts.append(f"\n\n현재 코드:\n```{file_name or 'vue'}\n{source_code}\n```")
    if error_info:
        context_parts.append(f"\n\n에러 정보:\n{error_info}")
    
    full_question = "\n".join(context_parts)

    initial_messages = [
        {"role": "system", "content": AGENT_SYSTEM_PROMPT},
        HumanMessage(content=full_question),
    ]

    collected_content = []
    
    async for event in _graph.astream_events(
        {"messages": initial_messages},
        version="v1"
    ):
        kind = event["event"]
        
        # 노드 시작
        if kind == "on_chain_start":
            name = event.get("name", "")
            if name == "agent":
                yield {"type": "step", "step": "analyzing", "message": "질문 분석 중..."}
            elif name == "tools":
                yield {"type": "step", "step": "searching", "message": "문서 검색 중..."}
        
        # 노드 종료
        elif kind == "on_chain_end":
            name = event.get("name", "")
            if name == "tools":
                yield {"type": "step", "step": "generating", "message": "답변 생성 중..."}
        
        # LLM 토큰 스트리밍
        elif kind == "on_chat_model_stream":
            chunk = event["data"]["chunk"]
            if hasattr(chunk, "content") and chunk.content:
                collected_content.append(chunk.content)
                yield {"type": "token", "content": chunk.content}
    
    # 최종 결과 파싱
    full_content = "".join(collected_content)
    if full_content:
        parsed = _parse_response(full_content)
        yield {
            "type": "result",
            "answer": parsed["answer"],
            "code_suggestions": parsed.get("code_suggestions")
        }
    else:
        yield {"type": "result", "answer": "답변을 생성하지 못했습니다.", "code_suggestions": None}


if __name__ == "__main__":
    result = run_agent("레이어 추가 방법은?")
    print("\n===== 최종 답변 =====\n")
    print("answer:", result["answer"])
    if result.get("code_suggestions"):
        print("\ncode_suggestions:", json.dumps(result["code_suggestions"], ensure_ascii=False, indent=2))
