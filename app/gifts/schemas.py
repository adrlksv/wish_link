from pydantic import BaseModel


class SGift(BaseModel):
    name: str
    gift_link: str
    photo_link: str
    description: str
    price: int
