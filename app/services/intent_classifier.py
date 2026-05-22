"""키워드 기반 intent 빠른 분류기.

확신이 있는 경우(명확한 키워드 또는 구조 시그널)에만 분류 결과를 반환하고,
애매하면 None을 반환하여 호출자가 LLM 폴백을 쓰도록 한다.
"""

from __future__ import annotations

import re
from typing import Optional


_ERROR_KEYWORDS = re.compile(
    r"(에러|오류|exception|traceback|stack\s*trace|디버깅|실패했|작동\s*안|동작\s*안)",
    re.IGNORECASE,
)
_CODE_KEYWORDS = re.compile(
    r"(예제|샘플|만들어\s*줘|구현해|코드\s*(작성|만들|짜)|sample\s*code|코드를\s*제공)",
    re.IGNORECASE,
)
_RAG_KEYWORDS = re.compile(
    r"(란\??$|이란\??$|뭐(야|예요|입니까)|무엇(이|인가)|설명해|차이(가|는|점)|종류|개념)",
    re.IGNORECASE,
)


def classify_by_keywords(
    content: str, has_source_code: bool = False, has_error_info: bool = False
) -> Optional[str]:
    """키워드/구조 기반 빠른 분류. 확신이 없으면 None 반환."""
    if has_error_info or _ERROR_KEYWORDS.search(content):
        return "error_analysis"
    if has_source_code:
        return "code_generation"
    if _CODE_KEYWORDS.search(content):
        return "code_generation"
    if _RAG_KEYWORDS.search(content):
        return "rag_search"
    return None
