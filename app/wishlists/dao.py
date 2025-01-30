from sqlalchemy import select, insert

from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.wishlists.models import Wishlist

from datetime import date


class WishlistDAO(BaseDAO):
    model = Wishlist

    @classmethod
    async def get_wishlist(
        cls,
        user_id: int
    ):
        async with async_session_maker() as session:
            query = select(Wishlist).where(user_id == Wishlist.user_id)
            result = await session.execute(query)

            return result.scalars().all()
        
    @classmethod
    async def add_wishlist(
        cls,
        user_id: int,
        name: str,
        to_date: date
    ):
        async with async_session_maker() as session:
            query = insert(Wishlist).values({
                "user_id": user_id,
                "name": name,
                "to_date": to_date
            })
            
            await session.execute(query)
            await session.commit()

            return {
                "message": "success"
            }
    