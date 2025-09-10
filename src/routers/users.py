# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter, HTTPException, status, Response
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
from typing import Optional

# import local modules
from lib.models import ProfileType, jwtPayload, GenerateID
from routers.auth import genJWT
from sqlOps.users.sqlRead import sqlCheckID, sqlCheckUsername, sqlCheckEmail, sqlGetUserInfo, sqlGetUsername
from sqlOps.users.sqlWrite import sqlCreateAccount, sqlPatchAccount

# load environment variables
load_dotenv()
SERVER_NAME = os.getenv('SERVER_NAME')

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_user(userID: str):
    info = sqlGetUserInfo(userID)[0]
    if info:
        rp = {
            "userID":info[0],
            "username":info[1],
            "password":info[2],
            "birthday":info[3],
            "email":info[4],
            "bio":info[5],
            "follows":info[6]
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rp))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

class ProfileRead(BaseModel):
    userID: str
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    bio: Optional[str] = None

class ProfilePatch(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    bio: Optional[str] = None

@router.patch("/", response_model=ProfileRead)
async def patch_user(userID: str, patch: ProfilePatch):
    update_data = patch.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update.")
    
    # safety checks
    # check if username or email are taken
    if patch.email:
        if sqlCheckEmail(patch.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is Taken")
    if patch.username:
        if sqlCheckUsername(patch.username):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is Taken")
    for key, value in update_data.items():
        sqlPatchAccount(userID=userID, attribute=key, value=value)
    
    return Response( status_code=status.HTTP_204_NO_CONTENT )


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

@router.get("/username")
async def get_user(userID: str):
    info = sqlGetUsername(userID)[0]
    if info:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(info))
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")