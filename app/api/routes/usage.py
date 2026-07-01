"""사용자별 토큰 사용량 조회 API.

일별 리셋을 전제로 '오늘 사용량'과 '누적 사용량', 그리고 일자별 추이를 제공한다.
('오늘' 기준은 DB 세션 타임존의 current_date 기준)
"""
from datetime import date, datetime, timedelta
from typing import List, Literal, Optional, Tuple

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import Date, cast, func
from sqlalchemy.orm import Session

from app.core.auth import get_current_user, require_admin
from app.db.database import get_db
from app.db.models import TokenUsage

router = APIRouter(prefix="/usage", tags=["Usage"])


class UsageStat(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    cost_usd: float = 0.0
    llm_calls: int = 0


class UsageSummary(BaseModel):
    user_id: str
    today: UsageStat
    total: UsageStat


class DailyUsage(UsageStat):
    date: date


class DailyUsageResponse(BaseModel):
    user_id: str
    daily: List[DailyUsage]


def _aggregate(db: Session, user_id: str, *filters) -> UsageStat:
    row = (
        db.query(
            func.coalesce(func.sum(TokenUsage.input_tokens), 0),
            func.coalesce(func.sum(TokenUsage.output_tokens), 0),
            func.coalesce(func.sum(TokenUsage.total_tokens), 0),
            func.coalesce(func.sum(TokenUsage.cost_usd), 0),
            func.count(TokenUsage.id),
        )
        .filter(TokenUsage.user_id == user_id, *filters)
        .one()
    )
    return UsageStat(
        input_tokens=int(row[0]),
        output_tokens=int(row[1]),
        total_tokens=int(row[2]),
        cost_usd=float(row[3]),
        llm_calls=int(row[4]),
    )


@router.get(
    "/me",
    response_model=UsageSummary,
    summary="내 토큰 사용량 요약",
    description="오늘(일별 리셋 기준) 및 누적 토큰 사용량과 예상 비용을 반환",
)
def my_usage(
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):
    today = _aggregate(
        db, user_id, cast(TokenUsage.created_at, Date) == func.current_date()
    )
    total = _aggregate(db, user_id)
    return UsageSummary(user_id=user_id, today=today, total=total)


@router.get(
    "/me/daily",
    response_model=DailyUsageResponse,
    summary="내 일자별 토큰 사용량",
    description="최근 N일간 일자별 토큰 사용량/비용 추이 (기본 30일)",
)
def my_daily_usage(
    days: int = Query(30, ge=1, le=365),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):
    since = func.current_date() - timedelta(days=days - 1)
    day_col = cast(TokenUsage.created_at, Date).label("day")
    rows = (
        db.query(
            day_col,
            func.coalesce(func.sum(TokenUsage.input_tokens), 0),
            func.coalesce(func.sum(TokenUsage.output_tokens), 0),
            func.coalesce(func.sum(TokenUsage.total_tokens), 0),
            func.coalesce(func.sum(TokenUsage.cost_usd), 0),
            func.count(TokenUsage.id),
        )
        .filter(TokenUsage.user_id == user_id, cast(TokenUsage.created_at, Date) >= since)
        .group_by(day_col)
        .order_by(day_col.desc())
        .all()
    )
    daily = [
        DailyUsage(
            date=r[0],
            input_tokens=int(r[1]),
            output_tokens=int(r[2]),
            total_tokens=int(r[3]),
            cost_usd=float(r[4]),
            llm_calls=int(r[5]),
        )
        for r in rows
    ]
    return DailyUsageResponse(user_id=user_id, daily=daily)


# ---------------------------------------------------------------------------
# 관리자 집계 (회원등급 >= 70)
# ---------------------------------------------------------------------------

Period = Literal["day", "week", "month"]


def _split_user_id(user_id: str) -> Tuple[Optional[int], Optional[str]]:
    """user_id 를 ':' 기준으로 '<dmn_no>:<login_id>' 로 분해.

    앞 토막이 정수면 dmn_no(int), 뒤 토막을 login_id 로 본다.
    형식이 다르거나 앞 토막이 정수가 아니면 (None, None) 을 반환하고
    호출 측에서 user_id 원문을 그대로 노출한다.
    """
    parts = user_id.split(":", 1)
    if len(parts) != 2:
        return None, None
    head, login_id = parts
    try:
        return int(head), login_id
    except ValueError:
        return None, None


def _date_range_filters(start: date, end: date):
    """[start, end] 를 created_at 기준 반열린 구간 [start, end+1day) 필터로 변환."""
    end_exclusive = end + timedelta(days=1)
    return (
        TokenUsage.created_at >= start,
        TokenUsage.created_at < end_exclusive,
    )


class AdminTotals(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    cost_usd: float = 0.0
    llm_calls: int = 0


class AdminAggregateRow(BaseModel):
    user_id: str
    dmn_no: Optional[int] = None
    login_id: Optional[str] = None
    bucket: str
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    cost_usd: float = 0.0
    llm_calls: int = 0


class AdminAggregateResponse(BaseModel):
    period: Period
    start: date
    end: date
    rows: List[AdminAggregateRow]
    totals: AdminTotals
    page: int
    size: int
    has_more: bool


class AdminUserRow(BaseModel):
    user_id: str
    dmn_no: Optional[int] = None
    login_id: Optional[str] = None
    total_tokens: int = 0
    cost_usd: float = 0.0
    llm_calls: int = 0
    last_used: Optional[datetime] = None


class AdminUsersTotals(BaseModel):
    total_tokens: int = 0
    cost_usd: float = 0.0
    llm_calls: int = 0


class AdminUsersResponse(BaseModel):
    rows: List[AdminUserRow]
    totals: AdminUsersTotals
    page: int
    size: int
    has_more: bool


@router.get(
    "/admin/aggregate",
    response_model=AdminAggregateResponse,
    summary="[관리자] 기간 버킷별 토큰 사용량 집계",
    description=(
        "회원등급 70 이상 전용. period(day/week/month) 버킷 × 사용자별 "
        "토큰/비용/호출수 집계. 날짜는 반열린 구간 [start, end] 적용."
    ),
)
def admin_aggregate(
    period: Period = Query("day", description="집계 단위 (day|week|month)"),
    start: date = Query(..., description="시작일 YYYY-MM-DD (포함)"),
    end: date = Query(..., description="종료일 YYYY-MM-DD (포함)"),
    user_id: Optional[str] = Query(None, description="특정 user_id 로 한정(선택)"),
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=500),
    db: Session = Depends(get_db),
    _: str = Depends(require_admin),
):
    bucket = cast(func.date_trunc(period, TokenUsage.created_at), Date).label("bucket")
    filters = list(_date_range_filters(start, end))
    if user_id:
        filters.append(TokenUsage.user_id == user_id)

    base = (
        db.query(
            TokenUsage.user_id.label("user_id"),
            bucket,
            func.coalesce(func.sum(TokenUsage.input_tokens), 0),
            func.coalesce(func.sum(TokenUsage.output_tokens), 0),
            func.coalesce(func.sum(TokenUsage.total_tokens), 0),
            func.coalesce(func.sum(TokenUsage.cost_usd), 0),
            func.count(TokenUsage.id),
        )
        .filter(*filters)
        .group_by(TokenUsage.user_id, bucket)
        .order_by(bucket.desc(), TokenUsage.user_id)
    )

    offset = (page - 1) * size
    # has_more 판정을 위해 size + 1 건 조회
    fetched = base.offset(offset).limit(size + 1).all()
    has_more = len(fetched) > size
    page_rows = fetched[:size]

    rows: List[AdminAggregateRow] = []
    for r in page_rows:
        dmn_no, login_id = _split_user_id(r[0])
        rows.append(
            AdminAggregateRow(
                user_id=r[0],
                dmn_no=dmn_no,
                login_id=login_id,
                bucket=r[1].isoformat(),
                input_tokens=int(r[2]),
                output_tokens=int(r[3]),
                total_tokens=int(r[4]),
                cost_usd=float(r[5]),
                llm_calls=int(r[6]),
            )
        )

    trow = (
        db.query(
            func.coalesce(func.sum(TokenUsage.input_tokens), 0),
            func.coalesce(func.sum(TokenUsage.output_tokens), 0),
            func.coalesce(func.sum(TokenUsage.total_tokens), 0),
            func.coalesce(func.sum(TokenUsage.cost_usd), 0),
            func.count(TokenUsage.id),
        )
        .filter(*filters)
        .one()
    )
    totals = AdminTotals(
        input_tokens=int(trow[0]),
        output_tokens=int(trow[1]),
        total_tokens=int(trow[2]),
        cost_usd=float(trow[3]),
        llm_calls=int(trow[4]),
    )

    return AdminAggregateResponse(
        period=period,
        start=start,
        end=end,
        rows=rows,
        totals=totals,
        page=page,
        size=size,
        has_more=has_more,
    )


@router.get(
    "/admin/users",
    response_model=AdminUsersResponse,
    summary="[관리자] 사용자별 누적 토큰 사용량",
    description=(
        "회원등급 70 이상 전용. 기간 내 user_id 별 누적 토큰/비용/호출수와 "
        "마지막 사용시각을 집계."
    ),
)
def admin_users(
    start: date = Query(..., description="시작일 YYYY-MM-DD (포함)"),
    end: date = Query(..., description="종료일 YYYY-MM-DD (포함)"),
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=500),
    db: Session = Depends(get_db),
    _: str = Depends(require_admin),
):
    filters = list(_date_range_filters(start, end))

    base = (
        db.query(
            TokenUsage.user_id.label("user_id"),
            func.coalesce(func.sum(TokenUsage.total_tokens), 0),
            func.coalesce(func.sum(TokenUsage.cost_usd), 0),
            func.count(TokenUsage.id),
            func.max(TokenUsage.created_at),
        )
        .filter(*filters)
        .group_by(TokenUsage.user_id)
        .order_by(func.coalesce(func.sum(TokenUsage.total_tokens), 0).desc(), TokenUsage.user_id)
    )

    offset = (page - 1) * size
    fetched = base.offset(offset).limit(size + 1).all()
    has_more = len(fetched) > size
    page_rows = fetched[:size]

    rows: List[AdminUserRow] = []
    for r in page_rows:
        dmn_no, login_id = _split_user_id(r[0])
        rows.append(
            AdminUserRow(
                user_id=r[0],
                dmn_no=dmn_no,
                login_id=login_id,
                total_tokens=int(r[1]),
                cost_usd=float(r[2]),
                llm_calls=int(r[3]),
                last_used=r[4],
            )
        )

    trow = (
        db.query(
            func.coalesce(func.sum(TokenUsage.total_tokens), 0),
            func.coalesce(func.sum(TokenUsage.cost_usd), 0),
            func.count(TokenUsage.id),
        )
        .filter(*filters)
        .one()
    )
    totals = AdminUsersTotals(
        total_tokens=int(trow[0]),
        cost_usd=float(trow[1]),
        llm_calls=int(trow[2]),
    )

    return AdminUsersResponse(
        rows=rows,
        totals=totals,
        page=page,
        size=size,
        has_more=has_more,
    )
