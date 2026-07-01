from __future__ import annotations

from typing import List, Optional, Literal

import tiktoken
from pydantic import BaseModel, Field, field_validator


MAX_SOURCE_CODE_TOKENS = 8000

_TOKEN_ENCODER = None


def _count_tokens(text: str) -> int:
    global _TOKEN_ENCODER
    if _TOKEN_ENCODER is None:
        _TOKEN_ENCODER = tiktoken.get_encoding("o200k_base")
    return len(_TOKEN_ENCODER.encode(text))


class AskRequest(BaseModel):
    conversation_id: Optional[str] = Field(None, description="대화 세션 ID (없으면 새로 생성)")
    question: str = Field(..., min_length=1, description="질문 내용")
    source_code: Optional[str] = Field(None, description="현재 편집 중인 소스코드")
    file_name: Optional[str] = Field(None, description="파일명")
    error_info: Optional[str] = Field(None, description="에러 정보")
    # history는 이제 Redis에서 자동으로 가져오므로 제거

    @field_validator("question")
    @classmethod
    def _validate_question_length(cls, v: str) -> str:
        if len(v) > 2000:
            raise ValueError(
                f"질문이 너무 깁니다 ({len(v)}자 / 최대 2000자). 코드는 에디터에 두고 질문만 간략히 작성해주세요."
            )
        return v

    @field_validator("source_code")
    @classmethod
    def _validate_source_code_tokens(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        token_count = _count_tokens(v)
        if token_count > MAX_SOURCE_CODE_TOKENS:
            raise ValueError(
                f"코드가 너무 깁니다 ({token_count}토큰 / 최대 {MAX_SOURCE_CODE_TOKENS}토큰). "
                f"질문과 관련된 함수나 부분만 보내주세요."
            )
        return v


class StreamEvent(BaseModel):
    """Streaming 이벤트"""
    type: Literal["start", "step", "token", "result", "error", "done"]
    step: Optional[Literal["analyzing", "searching", "generating", "validating"]] = None
    message: Optional[str] = None
    content: Optional[str] = None
    answer: Optional[str] = None
    code_suggestions: Optional[List[dict]] = None


class CodeSuggestion(BaseModel):
    filename: str = Field(..., description="대상 파일명 (예: App.vue, stores/appStore.js)")
    language: str = Field(..., description="언어 (vue, js, ts, html, css)")
    action: str = Field(default="auto", description="적용 방식 (replace_file, insert_function, insert_script, auto)")
    code: str = Field(..., description="전체 파일 코드 (마크다운 코드블록 없이 순수 코드)")
    description: Optional[str] = Field(None, description="이 코드가 뭘 하는지 한줄 설명")
    label: Optional[str] = Field(None, description="실행 가능한 기능일 때 앱 패널에 추가할 버튼의 한글 라벨 (예: '서울로 이동'). 설정 시 Apply하면 이 함수를 호출하는 버튼이 앱에 같이 추가됩니다.")


class AskResponse(BaseModel):
    conversation_id: str = Field(..., description="대화 세션 ID")
    answer: str = Field(..., description="생성된 답변 (코드 설명만, 코드 자체는 code_suggestions에)")
    code_suggestions: Optional[List[CodeSuggestion]] = Field(
        None, description="코드 제안 목록. 코드 제안이 없으면 필드 자체를 생략"
    )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "answer": "카메라를 이동하려면 moveCamera 함수를 사용하세요.",
                },
                {
                    "answer": "지도 위에 마커를 추가하는 코드입니다.",
                    "code_suggestions": [
                        {
                            "filename": "App.vue",
                            "language": "vue",
                            "code": "<template>\n  <div id=\"map\"></div>\n</template>",
                            "description": "마커 추가 컴포넌트",
                        }
                    ],
                },
            ]
        }


class InterruptedResponse(BaseModel):
    """Human-in-the-Loop 중단 응답"""
    interrupted: bool = Field(True, description="중단 여부")
    thread_id: str = Field(..., description="재개용 스레드 ID")
    conversation_id: str = Field(..., description="대화 세션 ID")
    context: str = Field(..., description="검색된 문서 컨텍스트")
    intent: str = Field(..., description="의도 분류 결과")
    next_node: Optional[str] = Field(None, description="다음 실행 노드")
    message: str = Field(default="코드 생성 전 검색된 문서를 확인하세요. /api/v1/ask/resume로 계속 진행하세요.", description="안내 메시지")


class ErrorResponse(BaseModel):
    detail: str = Field(..., description="에러 메시지")



class AskAsyncResponse(BaseModel):
    """비동기 요청 응답"""
    request_id: str = Field(..., description="요청 ID (결과 조회용)")
    conversation_id: str = Field(..., description="대화 세션 ID")
    status: str = Field(default="processing", description="처리 상태")


class ResultResponse(BaseModel):
    """결과 조회 응답"""
    request_id: str
    status: Literal["processing", "completed", "error"]
    conversation_id: Optional[str] = None
    answer: Optional[str] = None
    code_suggestions: Optional[List[CodeSuggestion]] = None
    error: Optional[str] = None
