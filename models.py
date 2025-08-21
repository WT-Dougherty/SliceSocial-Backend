from pydantic import BaseModel
import random, string

DEFAULT_PROFILE_PHOTO = 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'

def GenerateID(n):
    return ''.join( random.choice(string.ascii_letters + string.digits) for _ in range(n) )

class DateType(BaseModel):
    day: str
    month: str
    year: str

class ProfileType(BaseModel):
    userID: str | None = GenerateID(8)
    username: str
    password: str
    birthday: DateType
    email: str

    profilePicture: str | None = DEFAULT_PROFILE_PHOTO
    bio: str | None = ''

    followers: list[str]
    followCount: int