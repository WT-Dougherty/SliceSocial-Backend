from pydantic import BaseModel
from typing import Optional
import random, string
from datetime import datetime
from dateutil import parser

DEFAULT_PROFILE_PHOTO = 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'

def GenerateID(n):
    return ''.join( random.choice(string.ascii_letters + string.digits) for _ in range(n) )
def GenerateTimestamp():
    dt: datetime = datetime.now()
    formatted_date_time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return parser.isoparse(formatted_date_time)

# ----------------- FOR PROFILE OBJECTS -----------------
class DateType(BaseModel):
    day: str
    month: str
    year: str
class TimeType(BaseModel):
    seconds: int
    minutes: int
    hours: int
class ProfileType(BaseModel):
    userID: str | None = GenerateID(16)
    username: str
    password: str
    birthday: DateType
    email: str

    profilePicture: str | None = DEFAULT_PROFILE_PHOTO
    bio: str | None = ''

    follow_list: list[str] | None = []
    follows: int

# ----------------- POSTS -----------------
class PostType(BaseModel):
    postID: str
    userID: str
    username: str
    caption: Optional[str] = ''
    posted_at: str
    comment_count: Optional[int] = 0
    like_count: Optional[int] = 0

# ----------------- COMMENTS -----------------
class CommentType(BaseModel):
    postID: str
    commentID: Optional[str] = ''
    username: str
    comment: str
    posted_at: Optional[str] = ''

# ----------------- AUTHORIZATION -----------------
class jwtPayload(BaseModel):
    iss: str
    sub: str
    aud: str
    iat: int
    exp: int
    nbf: int
class loginParams(BaseModel):
    username: str
    password: str