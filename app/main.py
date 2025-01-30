from fastapi import FastAPI

from app.users.router import router as user_router
from app.wishlists.router import router as wishlist_router
from app.wishlists.router import router as gift_router


app = FastAPI()

app.include_router(user_router)
app.include_router(wishlist_router)
app.include_router(gift_router)
