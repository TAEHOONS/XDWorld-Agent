# 프론트엔드 적용 가이드 — 토큰 사용량 측정

XDWorld Agent 백엔드에 **사용자별 토큰 사용량 측정**이 추가되었습니다.
프론트엔드가 적용해야 할 변경은 **① 신규 사용량 조회 API 2개**와 **② `/ask/resume` 인증 필수화(주의: 깨질 수 있음)** 두 가지입니다.

> 공통: 모든 엔드포인트는 기존과 동일하게 `Authorization: Bearer <JWT>` 헤더가 필요합니다.
> base URL 접두사: `/api/v1`

---

## ⚠️ ① (Breaking) `POST /api/v1/ask/resume` 인증 필수화

코드 생성(HITL) 재개 엔드포인트가 이제 **`Authorization` 헤더를 요구**합니다.
헤더 없이 호출하면 **401**이 반환됩니다. (사용량을 호출 사용자에게 귀속시키기 위함)

**기존 코드에서 `/ask/resume` 호출 시 토큰 헤더가 빠져 있으면 추가해야 합니다.**

요청 파라미터(쿼리스트링)와 SSE 응답 형식은 그대로입니다.

```
POST /api/v1/ask/resume?thread_id=<id>&approved=true&additional_context=<옵션>
Authorization: Bearer <JWT>      ← 추가 필요
Accept: text/event-stream
```

---

## ② (신규) 사용량 조회 API

### 2-1. 내 사용량 요약 — `GET /api/v1/usage/me`

오늘(일별 리셋 기준)과 누적 사용량/예상 비용을 반환합니다.

**Request**
```
GET /api/v1/usage/me
Authorization: Bearer <JWT>
```

**Response 200**
```json
{
  "user_id": "user-123",
  "today": {
    "input_tokens": 1820,
    "output_tokens": 540,
    "total_tokens": 2360,
    "cost_usd": 0.000597,
    "llm_calls": 6
  },
  "total": {
    "input_tokens": 81230,
    "output_tokens": 24110,
    "total_tokens": 105340,
    "cost_usd": 0.026652,
    "llm_calls": 214
  }
}
```

| 필드 | 의미 |
|------|------|
| `input_tokens` / `output_tokens` / `total_tokens` | 입력 / 출력 / 합계 토큰 수 |
| `cost_usd` | 사용 시점 단가로 산정한 예상 비용(USD) |
| `llm_calls` | 합산된 LLM 호출 건수 (질문 1회당 여러 건 발생) |
| `today` | 서버 타임존 기준 오늘 0시부터의 합계 |
| `total` | 가입 이후 전체 누적 |

> `cost_usd`는 USD입니다. 화면 표기 단위(₩ 등)는 프론트에서 환산하세요.

---

### 2-2. 일자별 추이 — `GET /api/v1/usage/me/daily`

최근 N일간 일자별 사용량을 반환합니다. (사용량 차트용)

**Request**
```
GET /api/v1/usage/me/daily?days=30
Authorization: Bearer <JWT>
```

| 쿼리 | 기본값 | 범위 |
|------|--------|------|
| `days` | 30 | 1 ~ 365 |

**Response 200** (날짜 내림차순, 사용 기록이 있는 날만 포함)
```json
{
  "user_id": "user-123",
  "daily": [
    { "date": "2026-06-02", "input_tokens": 1820, "output_tokens": 540, "total_tokens": 2360, "cost_usd": 0.000597, "llm_calls": 6 },
    { "date": "2026-06-01", "input_tokens": 9100, "output_tokens": 3020, "total_tokens": 12120, "cost_usd": 0.003177, "llm_calls": 28 }
  ]
}
```

> 사용이 없던 날짜는 배열에 포함되지 않습니다. 차트에서 빈 날을 0으로 채우려면 프론트에서 날짜 축을 생성해 매핑하세요.

---

## 프론트 적용 예시 (Nuxt 3 / `$fetch`)

```ts
// composables/useTokenUsage.ts
export function useTokenUsage() {
  const token = useAuthToken() // 프로젝트의 기존 JWT 취득 방식 사용

  const headers = () => ({ Authorization: `Bearer ${token.value}` })

  /** 내 사용량 요약 */
  const fetchUsage = () =>
    $fetch('/api/v1/usage/me', { headers: headers() })

  /** 일자별 추이 */
  const fetchDailyUsage = (days = 30) =>
    $fetch('/api/v1/usage/me/daily', { headers: headers(), query: { days } })

  return { fetchUsage, fetchDailyUsage }
}
```

```vue
<!-- 사용량 배지 예시 -->
<script setup lang="ts">
const { fetchUsage } = useTokenUsage()
const { data } = await useAsyncData('token-usage', () => fetchUsage())
</script>

<template>
  <div v-if="data" class="usage-badge">
    오늘 {{ data.today.total_tokens.toLocaleString() }} 토큰
    (${{ data.today.cost_usd.toFixed(4) }})
  </div>
</template>
```

---

## 참고 (다음 단계 예고)

향후 **관리자가 사용자별 토큰 한도를 설정**하고 초과 시 차단(HTTP **429**)하는 기능이 추가될 예정입니다.
그때 `/ask` 계열 요청이 429를 반환할 수 있으므로, **429 응답에 대한 사용자 안내 처리**를 미리 염두에 두면 좋습니다. (이번 변경에는 포함되지 않음)
