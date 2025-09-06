# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# import packages
from fastapi import APIRouter, status, Response, UploadFile
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
import io

# import local modules
from minioDB.s3read import s3get_pro_pic_image, s3get_post_image
from minioDB.s3write import s3add_profile_image, s3add_post_image

# load environment variables
load_dotenv()
SERVER_NAME = os.getenv('SERVER_NAME')

router = APIRouter(
    prefix="/images",
    tags=["images"]
)

@router.get('/propic')
async def get_pro_pic(userID):
    # get the post's image
    byte_image = s3get_pro_pic_image(userID)
    img_byte_array = io.BytesIO(byte_image)
    return StreamingResponse(img_byte_array, media_type="image/jpeg")

@router.post('/propic')
async def post_pro_pic( file : UploadFile, userID: str ):
    s3add_profile_image(file, userID)
    return Response(status_code=status.HTTP_201_CREATED)


@router.get('/post')
async def get_post_image(postID : str):
    # get the post's image
    byte_image = s3get_post_image(postID)
    img_byte_array = io.BytesIO(byte_image)
    return StreamingResponse(img_byte_array, media_type="image/jpeg")

@router.post('/post')
async def post_pro_pic( file : UploadFile, postID: str ):
    s3add_post_image(file, postID)
    return Response(status_code=status.HTTP_201_CREATED)