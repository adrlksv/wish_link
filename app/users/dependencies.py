from fastapi import Request, Depends

from app.config import settings
from app.users.dao import UserDAO

from datetime import datetime

from jose import JWTError, jwt

from app.exceptions import (
    TokenAbsentException,
    IncorrectTokenFormatException,
    TokenExpiredException,
    UserIsNotPresentException
)

def get_token(request: Request):
    token = request.cookies.get("wish_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < int(datetime.utcnow().timestamp())):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    
    return user
