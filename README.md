# 🌍 XDWorld Agent

XDWorld 지도 엔진 메뉴얼 기반 RAG(Retrieval-Augmented Generation) AI 어시스턴트입니다.

Markdown으로 작성된 XDWorld API 문서를 벡터화해 두고, 사용자의 자연어 질문을 **의도(Intent)별로 분류**한 뒤 관련 문서를 검색·재순위화하여 OpenAI GPT로 정확한 답변과 실행 가능한 코드를 생성합니다. 코드 생성 요청은 **Human-in-the-Loop**으로 사용자 승인을 거치며, 대화 히스토리·유사 대화·토큰 사용량을 PostgreSQL/Redis에 관리합니다.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-1C3C3C?logo=langchain&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-4169E1?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 데모

<p align="center">
  <img src="docs/images/screenshot.png" alt="XDWorld Agent 웹 UI" width="720" />
</p>

> 웹 브라우저에서 `http://localhost:8000` 으로 접속하면 채팅 UI를 사용할 수 있습니다.

---

## 핵심 기능

| 기능 | 설명 |
|------|------|
| **Intent 라우팅** | 질문을 `error_analysis` / `code_generation` / `rag_search` 로 분류. 키워드로 1차 판정하고 애매하면 LLM으로 폴백해 비용 절감 |
| **검색 품질 강화** | Query Expansion(질문 재작성) → FAISS 벡터 검색 → LLM Reranking(재순위화) 파이프라인 |
| **Human-in-the-Loop** | 코드 생성 요청은 답변 생성 직전에 중단하고, 검색된 문서를 사용자가 확인·승인한 뒤 재개 |
| **실행 가능한 코드 제안** | 답변 본문과 `code_suggestions`(파일/언어/액션/버튼 라벨 포함)를 분리해 반환 → 프론트에서 바로 적용 |
| **대화 컨텍스트** | 대화 세션·메시지를 PostgreSQL에 저장, 이전 히스토리와 **유사 과거 대화(pgvector)**를 컨텍스트로 활용 |
| **응답 방식 3종** | 동기(`/ask`), SSE 스트리밍(`/ask/stream`), 비동기 큐(`/ask/async` + Redis Pub/Sub) |
| **토큰 사용량 집계** | LLM 호출별 토큰/비용을 원장에 기록, 사용자별·관리자용 사용량 조회 API 제공 |
| **인증** | JWT Bearer 토큰(서명 검증은 외부 게이트웨이 담당, 본 서비스는 디코딩 후 `user_id` 추출) |

---

## 아키텍처

```
사용자 질문
    │
    ▼
┌──────────────────────────────┐
│  FastAPI (POST /api/v1/ask)  │  JWT 인증 · 대화세션 로드 · 메시지 저장
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────────────────────────────────┐
│  LangGraph Agent Pipeline (PostgreSQL Checkpoint)        │
│                                                          │
│  intent_router ──┬─► error_analysis ─┐                   │
│  (키워드→LLM)     ├─► code_generation ─┤─► [agent]        │
│                  └─► rag_search ──────┘   (최종 답변 생성) │
│                        │                                 │
│                        ▼                                 │
│         search_with_enhancement                          │
│         ① Query Expansion → ② FAISS 검색 → ③ Reranking    │
│                                                          │
│  * code_generation 은 agent 직전 중단(HITL) → 승인 후 재개 │
└──────────────────────────────────────────────────────────┘
               │
               ▼
   답변 + code_suggestions 반환 · 응답 저장 · 토큰사용량 기록
```

| 컴포넌트 | 설명 |
|---------|------|
| **FastAPI** | REST/SSE API 서버 및 정적 채팅 UI 서빙 |
| **LangGraph** | Intent 라우팅 + 검색 + 생성 워크플로우, PostgreSQL 체크포인트로 HITL 재개 지원 |
| **FAISS** | XDWorld 매뉴얼 문서 임베딩 벡터 저장 및 유사도 검색 |
| **PostgreSQL + pgvector** | 대화/메시지 저장, 유사 대화 검색, 토큰 사용량 원장 |
| **Redis** | 비동기 요청 결과 저장 및 Pub/Sub |
| **OpenAI** | 임베딩(embedding) · 의도 분류/재순위/답변 생성(chat) |

---

## 프로젝트 구조

```
xdworld-agent/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── ask.py           # /ask, /ask/stream, /ask/resume, /ask/async, /ask/result
│   │       ├── search.py        # /search/similar (유사 대화 검색)
│   │       └── usage.py         # /usage/me, /usage/admin/* (토큰 사용량)
│   ├── core/
│   │   ├── config.py            # 환경변수 설정 (pydantic-settings)
│   │   ├── auth.py              # JWT Bearer 인증 / 관리자 권한
│   │   ├── exceptions.py        # 커스텀 예외
│   │   └── logging.py           # 로깅 설정
│   ├── db/
│   │   ├── database.py          # SQLAlchemy 엔진/세션 (local·prod 프로파일)
│   │   ├── models.py            # Conversation / Message / MessageEmbedding / TokenUsage
│   │   └── redis_store.py       # 비동기 결과 저장 · Pub/Sub
│   ├── schemas/
│   │   └── chat.py              # 요청/응답 Pydantic 모델 (토큰 길이 검증 포함)
│   ├── services/
│   │   ├── graph.py             # LangGraph 파이프라인 (intent/검색/agent 노드, 스트리밍)
│   │   ├── intent_classifier.py # 키워드 기반 빠른 의도 분류
│   │   ├── retrieval.py         # Query Expansion + FAISS + Reranking
│   │   ├── vectorstore.py       # FAISS 벡터스토어 관리
│   │   ├── ingest.py            # Markdown → 벡터스토어 인제스트
│   │   ├── conversation.py      # 대화 세션/메시지/유사 대화 검색
│   │   ├── embedding.py         # 요약 임베딩 (text-embedding-3-small)
│   │   ├── response_parser.py   # 답변 → answer + code_suggestions 파싱
│   │   ├── prompts.py           # 시스템 프롬프트 템플릿
│   │   └── usage.py             # 토큰 사용량 콜백 수집기
│   ├── static/
│   │   └── index.html           # 채팅 웹 UI
│   └── main.py                  # FastAPI 앱 팩토리 · lifespan 초기화
├── data/
│   ├── raw_md/                  # XDWorld 메뉴얼 원본 Markdown
│   └── vectorstore/             # FAISS 인덱스 (인제스트 후 자동 저장)
├── scripts/                     # 마이그레이션/백필 스크립트
├── docker-compose.yml           # PostgreSQL(pgvector) + Redis + API
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 시작하기

### 사전 요구사항

- Python 3.11+
- OpenAI API Key
- PostgreSQL 16 (pgvector 확장) · Redis 7 — `docker-compose`로 함께 실행 가능

### 1. 저장소 클론

```bash
git clone https://github.com/Khaia/xdcloud_earth.git
cd xdcloud_earth/ai/xdworld-agent
```

### 2. 환경변수 설정

```bash
cp .env.example .env
```

`.env` 파일을 열어 OpenAI API 키를 입력합니다. (DB/Redis 기본값은 아래 docker-compose와 맞춰져 있습니다.)

```env
OPENAI_API_KEY="sk-your-api-key-here"
```

### 3. 의존 인프라 실행 (PostgreSQL + Redis)

```bash
docker compose up -d postgres redis
```

### 4. 가상환경 생성 및 의존성 설치

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 5. 벡터스토어 생성

`data/raw_md/` 의 Markdown 문서를 벡터화합니다:

```bash
python -m app.services.ingest
```

### 6. 서버 실행

```bash
uvicorn app.main:app --reload
```

브라우저에서 http://localhost:8000 으로 접속하세요.

> 전체 스택을 컨테이너로 한 번에 띄우려면 `docker compose up --build` 를 사용하세요.

---

## API

> 모든 `/api/v1/*` 엔드포인트는 `Authorization: Bearer <token>` 헤더가 필요합니다.

### `POST /api/v1/ask`

질문을 받아 파이프라인으로 답변을 생성합니다. 코드 생성 요청 시 HITL로 중단될 수 있습니다.

**Request**

```json
{
  "conversation_id": "선택 (없으면 새 세션 생성)",
  "question": "지도에 마커 추가하는 방법 알려줘",
  "source_code": "선택 (현재 편집 중인 코드, 최대 8000토큰)",
  "file_name": "App.vue",
  "error_info": "선택 (에러 메시지)"
}
```

**Response (완료)**

```json
{
  "conversation_id": "…",
  "answer": "지도 위에 마커를 추가하는 코드입니다.",
  "code_suggestions": [
    {
      "filename": "App.vue",
      "language": "vue",
      "action": "auto",
      "code": "<template> … </template>",
      "description": "마커 추가 컴포넌트",
      "label": "마커 추가"
    }
  ]
}
```

**Response (HITL 중단)** — 코드 생성 요청 시

```json
{
  "interrupted": true,
  "thread_id": "…",
  "conversation_id": "…",
  "context": "검색된 API 문서…",
  "intent": "code_generation"
}
```

### 기타 엔드포인트

| 메서드·경로 | 설명 |
|------------|------|
| `POST /api/v1/ask/stream` | LangGraph 단계(step)와 답변 토큰을 SSE로 실시간 스트리밍 |
| `POST /api/v1/ask/resume` | HITL 중단된 코드 생성 요청을 사용자 승인 후 SSE로 재개 |
| `POST /api/v1/ask/async` | 질문을 큐에 제출하고 `request_id` 즉시 반환 (Redis Pub/Sub) |
| `GET  /api/v1/ask/result/{request_id}` | 비동기 요청 결과 조회 |
| `GET  /api/v1/search/similar` | pgvector 기반 유사 과거 대화 검색 (사용자별 격리) |
| `GET  /api/v1/usage/me` | 내 오늘/누적 토큰 사용량·예상 비용 |
| `GET  /api/v1/usage/me/daily` | 내 일자별 사용량 추이 |
| `GET  /api/v1/usage/admin/aggregate` | (관리자, 등급≥70) 기간 버킷별 사용량 집계 |
| `GET  /api/v1/usage/admin/users` | (관리자, 등급≥70) 사용자별 누적 사용량 |
| `GET  /health` | 서버 상태 확인 |

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
| `RETRIEVER_K` | 벡터 검색 후보 문서 수 | `10` |
| `RERANK_TOP_K` | Reranking 후 최종 선택 문서 수 | `4` |
| `ACTIVE_PROFILE` | 실행 프로파일 (`local` / `prod`) | `local` |
| `DATABASE_URL_LOCAL` | 로컬 PostgreSQL 접속 URL | `postgresql+asyncpg://xdworld:xdworld@localhost:5432/xdworld_agent` |
| `DB_HOST` / `DB_PORT` / `DB_NAME` / `DB_USER` / `DB_PASSWORD` | 운영(`prod`) DB 접속 정보 | - |
| `REDIS_HOST` | 로컬 Redis URL | `redis://localhost:6379` |
| `CORS_ORIGINS` | 허용 CORS 오리진 (JSON 배열). `*` 포함 시 credentials 자동 비활성화 | `[]` |
| `LOG_LEVEL` | 로그 레벨 | `INFO` |

---

## 기술 스택

- **Backend**: FastAPI, Uvicorn/Gunicorn, Pydantic
- **AI/RAG**: LangChain, LangGraph (PostgreSQL Checkpoint), OpenAI API
- **Vector Store**: FAISS (문서), pgvector (유사 대화)
- **Database**: PostgreSQL 16, SQLAlchemy, Redis
- **Auth**: JWT (PyJWT)
- **Frontend**: Vanilla HTML/CSS/JavaScript

---

## 라이선스

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.
