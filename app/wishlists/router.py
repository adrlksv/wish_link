from fastapi import APIRouter, Depends, Query

from app.users.dependencies import get_current_user

from app.wishlists.dao import WishlistDAO
from app.users.models import User

from datetime import date, datetime


router = APIRouter(
    prefix="/wishlists",
    tags=["Wishlists"],
)


@router.get("")
async def get_wish(
    user: User = Depends(get_current_user)
):
    return await WishlistDAO.get_wishlist(user_id=user.id)


@router.post("")
async def add_wish(
    name: str = Query(..., description="День рождения"),
    to_date: date = Query(..., description=f"Например {datetime.now().date()}"),
    user: User = Depends(get_current_user)
):
    await WishlistDAO.add_wishlist(user.id, name, to_date)
