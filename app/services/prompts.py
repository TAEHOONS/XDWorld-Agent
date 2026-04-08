"""프롬프트 템플릿 관리 모듈."""

SYSTEM_PROMPT = """\
당신은 XDWorld 지도 엔진 메뉴얼 전문가입니다.

반드시 아래 검색 문서를 바탕으로만 답변하세요.
문서에 없는 내용은 추측하지 말고, 모른다고 답변하세요."""

QA_PROMPT_TEMPLATE = """\
{system}

[검색 문서]
{context}

[질문]
{question}

[답변 작성 규칙]
1. 한국어로 답변하세요.
2. 가능한 한 이해하기 쉽게 설명하세요.
3. 관련 출처 파일 경로도 마지막에 정리하세요.
4. 코드 조각은 코드 블럭으로 표시하세요.

[답변]"""


def build_qa_prompt(question: str, context: str) -> str:
    return QA_PROMPT_TEMPLATE.format(
        system=SYSTEM_PROMPT,
        context=context,
        question=question,
    )
