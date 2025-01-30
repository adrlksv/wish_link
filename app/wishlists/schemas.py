from pydantic import BaseModel

from datetime import date


class SWishlist(BaseModel):
    name: str
    to_date: date

    class Config:
        orm_mode = True
