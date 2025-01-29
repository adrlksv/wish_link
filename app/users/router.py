from fastapi import APIRouter, Depends, Response

from app.users.dependencies import get_current_user
from app.users.schemas import SUserRegister, SUserLogin
from app.users.dao import UserDAO
from app.users.auth import get_password_hash, authenticate_user
from app.users.auth import create_access_token
from app.users.models import User

from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException


router = APIRouter(
    prefix = "/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserDAO.find_one_or_none(email = user_data.email)
    
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(
        name=user_data.name,
        email=user_data.email,
        username=user_data.username, 
        hashed_password=hashed_password
    )


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("wish_access_token", access_token, httponly=True)

    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("wish_access_token")


@router.get("/me")
async def get_user(current_user: User = Depends(get_current_user)):
    return current_user
