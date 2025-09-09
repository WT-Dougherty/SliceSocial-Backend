from fastapi import FastAPI

from src.routers import users
from src.routers import posts
from src.routers import auth
from src.routers import images
from src.routers import connections
from src.routers import comments

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(images.router)
app.include_router(connections.router)
app.include_router(comments.router)