from sqlalchemy import Integer, String, Column, Date, ForeignKey

from app.database import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gift_count = Column(Integer)
    to_date = Column(Date)
    user_id = Column(ForeignKey("user.id"))
