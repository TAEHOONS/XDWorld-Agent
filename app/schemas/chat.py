from __future__ import annotations

from typing import List, Optional, Literal

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    conversation_id: Optional[str] = Field(None, description="대화 세션 ID (없으면 새로 생성)")
    question: str = Field(..., min_length=1, max_length=2000, description="질문 내용")
    source_code: Optional[str] = Field(None, description="현재 편집 중인 소스코드")
    file_name: Optional[str] = Field(None, description="파일명")
    error_info: Optional[str] = Field(None, description="에러 정보")
    # history는 이제 Redis에서 자동으로 가져오므로 제거


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
