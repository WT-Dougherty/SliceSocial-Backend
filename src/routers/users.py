# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter, HTTPException, status
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# import local modules
from lib.models import ProfileType, jwtPayload, GenerateID
from routers.auth import genJWT
from sqlOps.sqlRead import sqlCheckID, sqlCheckUsername, sqlCheckEmail
from sqlOps.sqlWrite import sqlCreateAccount

# load environment variables
load_dotenv()
SERVER_NAME = os.getenv('SERVER_NAME')

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users():
    return [{"id": 1, "name": "Alice"}]

@router.post("/create")
async def create_user(user: ProfileType):
    # generate unique ID
    new_id = GenerateID(16)
    while sqlCheckID(new_id):
        new_id = GenerateID(16)
    user.userID = new_id
    
    # safety checks
    # check if username or email are taken
    if sqlCheckEmail(user.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is Taken")
    if sqlCheckUsername(user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is Taken")

    # add user profile to db
    sqlCreateAccount(user)

    # create jsw
    payload = jwtPayload(
        iss=SERVER_NAME,
        sub=new_id,
        aud=SERVER_NAME,
        iat=0,
        exp=0,
        nbf=0
    )
    newJWT = genJWT(payload=payload)

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            {
                "access_token": newJWT,
                "token_type": "JWT",
                "expires_in": 2592000,
                "refresh_token": None,
            }
        )
    )