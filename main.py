from fastapi import FastAPI

from src.routers import users
from src.routers import auth

app = FastAPI()
app.include_router(users.router)
# app.include_router(posts.router)
app.include_router(auth.router)
