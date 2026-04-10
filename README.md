# 🌍 XDWorld Agent

XDWorld 지도 엔진 메뉴얼 기반 RAG(Retrieval-Augmented Generation) AI 어시스턴트입니다.

Markdown으로 작성된 XDWorld API 문서를 벡터화하고, 사용자의 자연어 질문에 대해 관련 문서를 검색한 뒤 OpenAI GPT를 통해 정확한 답변을 생성합니다.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?logo=langchain&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 데모

<p align="center">
  <img src="docs/images/screenshot.png" alt="XDWorld Agent 웹 UI" width="720" />
</p>

> 웹 브라우저에서 `http://localhost:8000` 으로 접속하면 채팅 UI를 사용할 수 있습니다.

---

## 아키텍처

```
사용자 질문
    │
    ▼
┌──────────────┐
│  FastAPI      │  POST /api/v1/ask
│  Web Server   │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│  LangGraph RAG Pipeline      │
│                              │
│  ① Retrieve ─► ② Generate   │
│     (FAISS)      (GPT)      │
└──────────────────────────────┘
       │
       ▼
   답변 반환
```

| 컴포넌트 | 설명 |
|---------|------|
| **FastAPI** | REST API 서버 및 정적 파일 서빙 |
| **LangGraph** | Retrieve → Generate 2단계 RAG 워크플로우 |
| **FAISS** | 문서 임베딩 벡터 저장 및 유사도 검색 |
| **OpenAI** | 텍스트 임베딩(embedding) 및 답변 생성(chat) |

---

## 프로젝트 구조

```
XDWorld-Agent/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── ask.py          # POST /api/v1/ask 엔드포인트
│   ├── core/
│   │   ├── config.py           # 환경변수 설정 (pydantic-settings)
│   │   ├── exceptions.py       # 커스텀 예외 클래스
│   │   └── logging.py          # 로깅 설정
│   ├── schemas/
│   │   └── chat.py             # 요청/응답 Pydantic 모델
│   ├── services/
│   │   ├── graph.py            # LangGraph RAG 파이프라인
│   │   ├── ingest.py           # Markdown → 벡터스토어 인제스트
│   │   ├── prompts.py          # 프롬프트 템플릿
│   │   └── vectorstore.py      # FAISS 벡터스토어 관리
│   ├── static/
│   │   └── index.html          # 채팅 웹 UI
│   └── main.py                 # FastAPI 앱 팩토리
├── data/
│   ├── raw_md/                 # XDWorld 메뉴얼 원본 Markdown
│   └── vectorstore/            # FAISS 인덱스 (생성 후 자동 저장)
├── .env.example                # 환경변수 템플릿
├── requirements.txt            # Python 의존성
└── README.md
```

---

## 시작하기

### 사전 요구사항

- Python 3.11+
- OpenAI API Key

### 1. 저장소 클론

```bash
git clone https://github.com/TAEHOONS/XDWorld-Agent.git
cd XDWorld-Agent
```

### 2. 가상환경 생성 및 의존성 설치

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 환경변수 설정

```bash
cp .env.example .env
```

`.env` 파일을 열고 OpenAI API 키를 입력합니다:

```env
OPENAI_API_KEY="sk-your-api-key-here"
OPENAI_MODEL="gpt-4o-mini"
OPENAI_TEMPERATURE=0.0
RETRIEVER_K=4
LOG_LEVEL="INFO"
CORS_ORIGINS='["*"]'
```

### 4. 벡터스토어 생성

`data/raw_md/` 디렉토리의 Markdown 문서를 벡터화합니다:

```bash
python -m app.services.ingest
```

### 5. 서버 실행

```bash
uvicorn app.main:app --reload
```

브라우저에서 http://localhost:8000 으로 접속하세요.

---

## API

### `POST /api/v1/ask`

질문을 받아 RAG 파이프라인으로 답변을 생성합니다.

**Request**

```json
{
  "question": "레이어 추가 방법은?"
}
```

**Response**

```json
{
  "question": "레이어 추가 방법은?",
  "answer": "레이어를 추가하려면 JSLayerList의 ..."
}
```

### `GET /health`

서버 상태를 확인합니다.

```json
{
  "status": "ok",
  "version": "1.0.0"
}
```

### API 문서

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 환경변수

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `OPENAI_API_KEY` | OpenAI API 키 (필수) | - |
| `OPENAI_MODEL` | 사용할 GPT 모델 | `gpt-4o-mini` |
| `OPENAI_TEMPERATURE` | 생성 온도 (0.0 = 결정적) | `0.0` |
| `RETRIEVER_K` | 검색할 문서 수 | `4` |
| `LOG_LEVEL` | 로그 레벨 | `INFO` |
| `CORS_ORIGINS` | 허용할 CORS 오리진 | `["*"]` |

---

## 기술 스택

- **Backend**: FastAPI, Uvicorn, Pydantic
- **AI/RAG**: LangChain, LangGraph, OpenAI API
- **Vector Store**: FAISS
- **Frontend**: Vanilla HTML/CSS/JavaScript

---

## 라이선스

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.
