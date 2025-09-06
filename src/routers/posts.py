# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter, HTTPException, status, Response
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from datetime import datetime

# import local modules
from lib.models import PostType
from sqlOps.posts.sqlRead import sqlGetProfilePosts
from sqlOps.posts.sqlWrite import sqlAddPost

# load environment variables
load_dotenv()
SERVER_NAME = os.getenv('SERVER_NAME')

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.get('/')
async def get_user_profile(userID: str):
    # to start, we will pull the post info from the relational db
    try:
        post_list = sqlGetProfilePosts(userID)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # now, we will create a list of post objects
    rl = []
    for post in post_list:
        dt : datetime = post[4]
        formatted_date_time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        print(formatted_date_time)
        rp = PostType(
            postID=post[0],
            userID=post[1],
            username=post[2],
            caption=post[3],
            posted_at= formatted_date_time,
            comment_count=post[5],
            like_count=post[6]
        )
        rl.append(rp)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rl))

@router.post('/')
async def add_post(post : PostType):
    try:
        sqlAddPost(post=post)
        return Response(status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)