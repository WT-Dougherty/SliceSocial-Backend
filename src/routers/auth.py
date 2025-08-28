# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import time
import jwt

# import local modules
from lib.models import jwtPayload, loginParams
from sqlOps.sqlRead import sqlAuthenticate

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# global variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
DB_USERS_READ = os.getenv('DB_USERS_READ')
SERVER_NAME = os.getenv('SERVER_NAME')
ALGORITHM = "HS256"

# function that creates jwt
def genJWT(payload : jwtPayload):
    payload.iat = int(time.time())
    payload.nbf = payload.iat
    payload.exp = payload.iat + (30 * 24 * 60 * 60)
    return jwt.encode(payload.model_dump(), SECRET_KEY, ALGORITHM)
    
# authentication endpoints
@router.post("/login")
async def authenticate(credentials : loginParams):
    print("Here")
    id = sqlAuthenticate(credentials.username, credentials.password)
    if id != None:
        payload = jwtPayload(
            iss=SERVER_NAME,
            sub=id,
            aud=SERVER_NAME,
            iat=0,
            exp=0,
            nbf=0
        )
        newJWT = genJWT(payload=payload)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                {
                    "access_token": newJWT,
                    "token_type": "JWT",
                    "expires_in": 2592000,
                    "refresh_token": None,
                }
            )
        )
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Login Credentials")