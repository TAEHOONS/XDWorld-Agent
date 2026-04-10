class VectorStoreNotFoundError(Exception):
    """벡터스토어가 존재하지 않을 때 발생"""


class DocumentLoadError(Exception):
    """문서 로드 실패 시 발생"""


class LLMError(Exception):
    """LLM 호출 실패 시 발생"""
