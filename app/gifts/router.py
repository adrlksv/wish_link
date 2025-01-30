from fastapi import APIRouter, Depends

from app.users.dependencies import get_current_user
from app.users.models import User
from app.gifts.schemas import SGift
from app.gifts.dao import GiftDAO

from typing import List


router = APIRouter(
    prefix="/gifts",
    tags=["Gifts"]
)


@router.get("")
async def get_gifts(
    wishlist_id: int,
    user: User = Depends(get_current_user)
) -> List[SGift]:
    await GiftDAO.get_gifts(wishlist_id)


@router.post("")
async def add_gifts(
    wishlist_id: int,
    *data: SGift,
    user: User = Depends(get_current_user)
):
    await GiftDAO.add_gifts(wishlist_id, *data)
