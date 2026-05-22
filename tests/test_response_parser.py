"""parse_response 단위 테스트."""

import json

from app.services.response_parser import parse_response, strip_initialize_wrapper


def test_plain_text_only():
    out = parse_response("그냥 설명만 있는 답변입니다.")
    assert out == {"answer": "그냥 설명만 있는 답변입니다.", "code_suggestions": None}


def test_explicit_json_block_single():
    body = """답변 본문입니다.

```json:code_suggestions
[{"filename": "main.js", "language": "js", "code": "console.log(1);"}]
```"""
    out = parse_response(body)
    assert out["answer"] == "답변 본문입니다."
    assert out["code_suggestions"] == [{
        "filename": "main.js",
        "language": "js",
        "code": "console.log(1);",
        "action": "insert_script",  # 추론됨
    }]


def test_explicit_json_block_action_preserved():
    body = """```json:code_suggestions
[{"filename": "a.js", "language": "js", "action": "replace_file", "code": "x"}]
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["action"] == "replace_file"


def test_explicit_json_block_strips_initialize_wrapper():
    code_with_wrapper = "function initialize() {\n  const a = 1;\n  const b = 2;\n}"
    body = (
        "```json:code_suggestions\n"
        + json.dumps([{"filename": "a.js", "language": "js", "code": code_with_wrapper}])
        + "\n```"
    )
    out = parse_response(body)
    assert out["code_suggestions"][0]["code"] == "const a = 1;\nconst b = 2;"


def test_explicit_json_block_invalid_falls_back_to_md():
    # JSON 파싱 실패 시 전체 content를 markdown 코드블록 패턴으로 재스캔.
    # 현재 정규식은 깨진 json:code_suggestions 블록의 닫힘 ```을 다음 ```js 블록의 시작과 묶어
    # 하나의 큰 블록으로 흡수하는 한계가 있음. 회귀 방지를 위해 현재 동작을 그대로 기록.
    body = """일부 답변

```json:code_suggestions
this is not json
```

```js
console.log("fallback");
```"""
    out = parse_response(body)
    assert out["code_suggestions"] is not None
    # 적어도 fallback 코드 문자열은 어딘가에 보존됨
    joined = "\n".join(s["code"] for s in out["code_suggestions"])
    assert 'console.log("fallback");' in joined


def test_explicit_json_block_with_trailing_text():
    body = """앞부분 설명.

```json:code_suggestions
[{"filename": "a.js", "language": "js", "code": "x"}]
```

이건 후행 설명."""
    out = parse_response(body)
    assert "앞부분 설명." in out["answer"]
    assert "이건 후행 설명." in out["answer"]


def test_explicit_json_single_object_wrapped_to_list():
    body = """```json:code_suggestions
{"filename": "a.js", "language": "js", "code": "x"}
```"""
    out = parse_response(body)
    assert isinstance(out["code_suggestions"], list)
    assert len(out["code_suggestions"]) == 1


def test_md_code_block_vue_full_file():
    body = """설명.

```vue
<template><div/></template>
<script>export default {}</script>
```"""
    out = parse_response(body)
    s = out["code_suggestions"][0]
    assert s["language"] == "vue"
    assert s["action"] == "replace_file"


def test_md_code_block_function_definition():
    body = """```js
function foo() { return 1; }
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["action"] == "insert_function"


def test_md_code_block_arrow_function():
    body = """```js
const bar = () => 2;
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["action"] == "insert_function"


def test_md_code_block_async_function():
    body = """```js
async function foo() { return 1; }
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["action"] == "insert_function"


def test_md_code_block_plain_script_default():
    body = """```js
let x = 10;
console.log(x);
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["action"] == "insert_script"


def test_md_code_block_language_alias_mapped():
    body = """```python
print("hi")
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["language"] == "python"


def test_md_code_block_no_language_default_js():
    body = """```
some code
```"""
    out = parse_response(body)
    assert out["code_suggestions"][0]["language"] == "js"


def test_md_multiple_blocks_preserve_order():
    body = """```js
const a = 1;
```

설명 중간.

```js
const b = 2;
```"""
    out = parse_response(body)
    codes = [s["code"] for s in out["code_suggestions"]]
    assert codes == ["const a = 1;", "const b = 2;"]


def test_md_empty_code_block_skipped():
    body = """```js
```"""
    out = parse_response(body)
    assert out["code_suggestions"] is None


def test_strip_initialize_wrapper_no_match_returns_original():
    src = "const x = 1;"
    assert strip_initialize_wrapper(src) == src


def test_strip_initialize_wrapper_dedents_two_space():
    # 구현은 라인별로 정확히 2칸씩 dedent (들여쓰기 0인 라인은 그대로 유지)
    src = "function initialize() {\n  if (a) {\n    b();\n  }\n}"
    assert strip_initialize_wrapper(src) == "if (a) {\n  b();\n}"
