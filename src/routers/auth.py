# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter
from dotenv import load_dotenv
import time
import jwt

# import local modules
from lib.models import jwtPayload

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
    payload.nbf = payload.iat
    payload.exp = payload.iat + (30 * 24 * 60 * 60)
    return jwt.encode(payload.model_dump(), SECRET_KEY, ALGORITHM)
    
# authentication endpoints
@router.post("/login")
async def authenticate():
    return