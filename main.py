from fastapi import FastAPI
from routers import users

USER_PROFILES_ENDPOINT = 'https://xsqio3ul1k.execute-api.us-east-2.amazonaws.com/development/userprofiles'

app = FastAPI()
app.include_router(users.router)