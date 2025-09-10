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
from lib.models import CommentType, GenerateID
from sqlOps.comments.sqlRead import sqlGetPostComments
from sqlOps.comments.sqlWrite import sqlAddComment, sqlRemoveComment

# load environment variables
load_dotenv()
SERVER_NAME = os.getenv('SERVER_NAME')

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.get('/')
async def get_post_comments(postID: str):
    # to start, we will pull the post info from the relational db
    try:
        comment_list = sqlGetPostComments(postID)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # now, we will create a list of post objects
    rl = []
    print(comment_list)
    if comment_list:
        for comment in comment_list:
            dt : datetime = comment[4]
            print(comment[4])
            print(dt)
            formatted_date_time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            rc = CommentType(
                postID=comment[0],
                commentID=comment[1],
                username=comment[2],
                comment=comment[3],
                posted_at= formatted_date_time,
            )
            rl.append(rc)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rl))

@router.post('/')
async def add_post(comment : CommentType):
    comment.commentID = GenerateID(16)
    try:
        sqlAddComment(comment=comment)
        return Response(status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.delete('/')
async def get_post_comments(commentID: str):
    try:
        sqlRemoveComment(commentID)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={})