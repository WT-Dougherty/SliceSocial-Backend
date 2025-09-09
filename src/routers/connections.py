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
from sqlOps.connections.sqlRead import sqlGetConnections
from sqlOps.connections.sqlWrite import sqlAddConnection

# load environment variables
load_dotenv()
SERVER_NAME = os.getenv('SERVER_NAME')

router = APIRouter(
    prefix="/connections",
    tags=["connections"]
)

@router.get('/')
async def get_connections(userID):
    connections = sqlGetConnections(userID=userID)
    return JSONResponse(status_code=200, content=jsonable_encoder(connections))