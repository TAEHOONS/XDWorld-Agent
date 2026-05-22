"""키워드 기반 intent 분류 단위 테스트."""

from app.services.intent_classifier import classify_by_keywords as classify


def test_error_info_struct_signal():
    assert classify("뭔가 안돼", has_source_code=False, has_error_info=True) == "error_analysis"


def test_source_code_signal_routes_to_code_gen():
    assert classify("이거 봐줘", has_source_code=True, has_error_info=False) == "code_generation"


def test_error_keyword_korean():
    assert classify("이 에러 왜 나요?") == "error_analysis"


def test_error_keyword_english():
    # XxxError 같은 영어 에러 이름은 의도적으로 키워드에서 제외 (false positive 우려)
    # → LLM 폴백이 처리하도록 None을 반환해야 함.
    # 단 "exception"이 명시되면 키워드로 잡힘.
    assert classify("TypeError 가 발생합니다") is None
    assert classify("exception이 떨어졌어요") == "error_analysis"


def test_error_keyword_traceback():
    assert classify("아래 traceback 봐줘") == "error_analysis"


def test_error_keyword_debug():
    assert classify("디버깅 도와줘") == "error_analysis"


def test_code_keyword_sample():
    assert classify("예제 보여줘") == "code_generation"


def test_code_keyword_make_request():
    assert classify("샘플 코드 만들어줘") == "code_generation"


def test_code_keyword_implementation():
    assert classify("이 기능 구현해줘") == "code_generation"


def test_rag_keyword_definition():
    assert classify("레이어란?") == "rag_search"


def test_rag_keyword_what_is():
    assert classify("XDWorld가 뭐야?") == "rag_search"


def test_rag_keyword_difference():
    assert classify("두 좌표계의 차이는?") == "rag_search"


def test_ambiguous_returns_none_for_llm_fallback():
    # 명확한 시그널이 없는 경우 None → LLM 폴백
    assert classify("XDWorld 카메라 이동") is None


def test_error_takes_priority_over_code():
    # 코드와 에러 키워드가 같이 있어도 에러 분석이 우선
    assert classify("이 코드 만들었는데 에러나요") == "error_analysis"


def test_priority_error_info_beats_source_code():
    # source_code가 있어도 error_info 시그널이 있으면 에러 분석으로
    assert classify("어떻게 하지", has_source_code=True, has_error_info=True) == "error_analysis"
