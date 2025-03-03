from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Gift(Base):
    __tablename__ = "gift"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gift_link: Mapped[str] = mapped_column(nullable=False)
    photo_link: Mapped[str]
    wishlist_id: Mapped[int] = mapped_column(ForeignKey("wishlist.id"))
    description: Mapped[str]
    price: Mapped[int]
