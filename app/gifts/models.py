from sqlalchemy import Integer, String, Column, ForeignKey

from app.database import Base


class Gift(Base):
    __tablename__ = "gift"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gift_link = Column(String, nullable=False)
    photo_link = Column(String)
    wishlist_id = Column(ForeignKey("wishlist.id"))
    description = Column(String)
    price = Column(Integer)
