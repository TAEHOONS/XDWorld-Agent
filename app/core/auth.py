import jwt
from fastapi import Header, HTTPException
from typing import Optional

def get_current_user(authorization: Optional[str] = Header(None)) -> str:
    """JWT 토큰에서 user_id 추출.

    서명 검증은 외부 게이트웨이가 담당하므로 본 서비스에선 디코딩만 수행.
    게이트웨이 우회 호출을 차단하기 위해 토큰 없는 요청은 401로 거부한다.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")

    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")

        payload = jwt.decode(token, options={"verify_signature": False})
        user_id = payload.get("sub") or payload.get("user_id") or payload.get("userId")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: no user_id")

        return str(user_id)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")


def require_admin(authorization: Optional[str] = Header(None)) -> str:
    """관리자 권한(회원등급 >= 70) 요구 디펜던시.

    get_current_user 와 동일하게 Bearer 토큰을 서명검증 없이 디코딩한다.
    (서명 검증은 외부 게이트웨이가 담당) payload 의 'mbr_grd_cd' 를 정수로
    해석해 70 미만이면 403. 토큰이 없으면 401.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")

    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")

        payload = jwt.decode(token, options={"verify_signature": False})
        user_id = payload.get("sub") or payload.get("user_id") or payload.get("userId")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: no user_id")

        try:
            grade = int(payload.get("mbr_grd_cd"))
        except (TypeError, ValueError):
            grade = 0

        if grade < 70:
            raise HTTPException(status_code=403, detail="Admin privilege required")

        return str(user_id)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
