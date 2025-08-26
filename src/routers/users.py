from fastapi import APIRouter
from models import ProfileType, DateType, jwtPayload, GenerateID
from auth import genJWT

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
    new_id = GenerateID(8)
    
    genJWT({
        sum: '69',
    })