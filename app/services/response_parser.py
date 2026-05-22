"""LLM 응답에서 답변 본문과 code_suggestions를 분리하는 파서.

우선순위:
1. ```json:code_suggestions ... ``` 명시 블록이 있으면 그것만 파싱
2. 없으면 일반 markdown 코드블록을 추출해 휴리스틱으로 action 추론
"""

from __future__ import annotations

import json
import re
from typing import Any, Dict

from app.core.logging import logger


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
_INITIALIZE_WRAPPER = re.compile(
    r'^\s*function\s+initialize\s*\(\s*\)\s*\{([\s\S]*)\}\s*$'
)
_FN_LEADING = re.compile(
    r"^(function\s+\w+|const\s+\w+\s*=\s*(async\s*)?\(|async\s+function\s+\w+)"
)


def strip_initialize_wrapper(code: str) -> str:
    """initialize() 함수로 감싸진 코드에서 내부 코드만 추출."""
    match = _INITIALIZE_WRAPPER.match(code.strip())
    if not match:
        return code
    inner = match.group(1).strip()
    lines = inner.split('\n')
    dedented = '\n'.join(l[2:] if l.startswith('  ') else l for l in lines)
    return dedented.strip()


def _infer_action(code: str, language: str) -> str:
    if language == "vue" and ("<template" in code or "<script" in code):
        return "replace_file"
    if _FN_LEADING.match(code):
        return "insert_function"
    return "insert_script"


def parse_response(content: str) -> Dict[str, Any]:
    """LLM 응답 본문을 {answer, code_suggestions}로 분리."""
    explicit = _EXPLICIT_PATTERN.search(content)
    if explicit:
        answer = content[: explicit.start()].strip()
        trailing = content[explicit.end():].strip()
        if trailing:
            answer = f"{answer}\n\n{trailing}" if answer else trailing
        try:
            suggestions = json.loads(explicit.group(1))
            if not isinstance(suggestions, list):
                suggestions = [suggestions]
            for s in suggestions:
                if isinstance(s.get("code"), str):
                    s["code"] = strip_initialize_wrapper(s["code"])
                if not s.get("action"):
                    s["action"] = _infer_action(s.get("code", ""), s.get("language", ""))
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
        action = _infer_action(code, language)
        suggestions.append({
            "filename": f"example.{language}" if language else "example.js",
            "language": language or "js",
            "action": action,
            "code": strip_initialize_wrapper(code),
        })
        answer = answer[: match.start()].rstrip() + answer[match.end():].lstrip()

    suggestions.reverse()
    return {"answer": answer.strip(), "code_suggestions": suggestions if suggestions else None}
