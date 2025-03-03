from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from datetime import date


from app.database import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gift_count: Mapped[int]
    to_date: Mapped[date]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
