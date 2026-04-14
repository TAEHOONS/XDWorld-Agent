from __future__ import annotations

from typing import List, Optional, Literal

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000, description="질문 내용")
    source_code: Optional[str] = Field(None, description="현재 편집 중인 소스코드")
    file_name: Optional[str] = Field(None, description="파일명")
    error_info: Optional[str] = Field(None, description="에러 정보")
    history: Optional[List[dict]] = Field(None, description="이전 대화 히스토리 [{role, content}]")


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
    code: str = Field(..., description="전체 파일 코드 (마크다운 코드블록 없이 순수 코드)")
    description: Optional[str] = Field(None, description="이 코드가 뭘 하는지 한줄 설명")


class AskResponse(BaseModel):
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


class ErrorResponse(BaseModel):
    detail: str = Field(..., description="에러 메시지")
