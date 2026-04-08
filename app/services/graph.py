"""LangGraph 기반 RAG 파이프라인."""

from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

from app.core.config import get_settings
from app.core.exceptions import LLMError
from app.core.logging import logger
from app.services.vectorstore import get_retriever
from app.services.prompts import build_qa_prompt


class GraphState(TypedDict):
    question: str
    documents: list[str]
    answer: str


def retrieve_node(state: GraphState) -> GraphState:
    question = state["question"]
    logger.info("검색 시작: %s", question[:80])

    retriever = get_retriever()
    docs = retriever.invoke(question)

    doc_texts = [
        f"[출처: {doc.metadata.get('relative_path', '')}]\n{doc.page_content}"
        for doc in docs
    ]
    logger.info("검색 완료: %d건", len(doc_texts))

    return {"question": question, "documents": doc_texts, "answer": ""}


def generate_node(state: GraphState) -> GraphState:
    settings = get_settings()
    question = state["question"]
    documents = state["documents"]

    llm = ChatOpenAI(
        model=settings.openai_model,
        api_key=settings.openai_api_key,
        temperature=settings.openai_temperature,
    )

    context = "\n\n".join(documents)
    prompt = build_qa_prompt(question, context)

    try:
        response = llm.invoke(prompt)
    except Exception as exc:
        logger.error("LLM 호출 실패: %s", exc)
        raise LLMError(f"LLM 호출 중 오류 발생: {exc}") from exc

    logger.info("답변 생성 완료 (%d자)", len(response.content))
    return {"question": question, "documents": documents, "answer": response.content}


def _build_graph():
    workflow = StateGraph(GraphState)
    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("generate", generate_node)
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)
    return workflow.compile()


_graph = _build_graph()


def run_agent(question: str) -> str:
    """질문을 받아 RAG 파이프라인을 실행하고 답변을 반환합니다."""
    if not question or not question.strip():
        raise ValueError("질문이 비어있습니다.")

    result = _graph.invoke(
        {"question": question.strip(), "documents": [], "answer": ""}
    )
    return result["answer"]


if __name__ == "__main__":
    answer = run_agent("레이어 추가 방법은?")
    print("\n===== 최종 답변 =====\n")
    print(answer)
