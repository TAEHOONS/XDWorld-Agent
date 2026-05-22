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
