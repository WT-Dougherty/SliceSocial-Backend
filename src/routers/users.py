# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

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
    if sqlCheckUsername(user.username):
        raise HTTPException(status_code=409, detail="Username is Taken")
    if sqlCheckEmail(user.email):
        raise HTTPException(status_code=409, detail="Email is Taken")

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

    return {
        "status-code": 201,
        "body": {
            "access_token": newJWT,
            "token_type": "JWT",
            "expires_in": 2592000,
            "refresh_token": None,
        }
    }