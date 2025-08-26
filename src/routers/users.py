import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from fastapi import APIRouter
from lib.models import ProfileType, DateType, jwtPayload, GenerateID
from routers.auth import genJWT
from sqlOps.sqlRead import sqlCheckID

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

birthday = DateType(day='18', month='June', year='2002')
profile = ProfileType(username='Will',
                      password='password',
                      birthday=birthday,
                      email='willtdougherty@gmail.com',
                      followers=[],
                      followCount=0)


@router.get("/")
async def get_users():
    return [{"id": 1, "name": "Alice"}]

@router.post("/create")
async def create_user(user: ProfileType):
    new_id = GenerateID(16)
    while not sqlCheckID(new_id):
        new_id = GenerateID(16)
    
    print(genJWT(payload={
        '69',
        '69',
        '69',
        0,
        0
    }))