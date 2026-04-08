from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000, description="질문 내용")


class AskResponse(BaseModel):
    question: str = Field(..., description="원본 질문")
    answer: str = Field(..., description="생성된 답변")


class ErrorResponse(BaseModel):
    detail: str = Field(..., description="에러 메시지")
