from pydantic import BaseModel

from typing import Optional


class SGift(BaseModel):
    name: str
    gift_link: str
    
    pass
