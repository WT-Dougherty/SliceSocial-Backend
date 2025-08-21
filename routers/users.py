from fastapi import APIRouter
from models import ProfileType, DateType

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

@router.post("/")
async def create_user(user: dict):
    return {"message": "User created", "user": user}