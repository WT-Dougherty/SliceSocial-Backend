import os

from fastapi import APIRouter
from dotenv import load_dotenv
from lib.models import jwtPayload
import time
import jwt

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# global variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
DB_USERS_READ = os.getenv('DB_USERS_READ')
ALGORITHM = "HS256"

# function that creates jwt
def genJWT(payload : jwtPayload):
    header = { "alg": ALGORITHM, "typ": "JWT" }
    payload.iat = int(time.time())
    payload.exp = payload.iat + (30 * 24 * 60 * 60)
    return jwt.encode(payload, SECRET_KEY, header["alg"])
    
# authentication endpoints
@router.post("/login")
async def authenticate():
    return