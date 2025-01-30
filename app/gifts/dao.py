from sqlalchemy import select, insert

from app.dao.base import BaseDAO
from app.gifts.models import Gift
from app.database import async_session_maker


class GiftDAO(BaseDAO):
    model = Gift

    @classmethod
    async def get_gifts(
        cls,
        wishlist_id,
    ):
        async with async_session_maker() as session:
            query = select(Gift).where(wishlist_id==Gift.wishlist_id)
            result = await session.execute(query)

            return result.scalars().all()
        
    @classmethod
    async def add_gifts(
        cls,
        name,
        gift_link,
        photo_link,
        description,
        price,
        wishlist_id
    ):
        async with async_session_maker() as session:
            query = insert(Gift).values({
                "wishlist_id": wishlist_id,
                "name": name,
                "gift_link": gift_link,
                "photo_link": photo_link,
                "description": description,
                "price": price
            })

            await session.execute(query)
            await session.commit()

            return {
                "message": "success"
            }
