from fastapi import APIRouter

from app.users.schemas import SUserRegister


router = APIRouter(
    prefix = "/auth",
    tags=["Auth"]
)


@router.post("/registration")
async def register_user(user_data: SUserRegister):
    pass
