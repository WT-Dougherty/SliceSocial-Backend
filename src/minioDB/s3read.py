from .conn import s3
from botocore.exceptions import ClientError
from fastapi import HTTPException, status

# get the image corresponding to post with postID=postID
def s3get_post_image(postID: str):
    try:
        obj = s3.get_object(Bucket="post-images", Key=postID)
    except ClientError as e:
        if e.response["Error"]["Code"] in ("NoSuchKey", "404"):
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data: bytes = obj["Body"].read()
    return data

# get the profile picture corresponding to user with userID=userID
def s3get_pro_pic_image(userID: str):
    try:
        obj = s3.get_object(Bucket="profile-images", Key=userID)
    except ClientError as e:
        if e.response["Error"]["Code"] in ("NoSuchKey", "404"):
            obj = s3.get_object(Bucket="profile-images", Key="defaultpropicgry")

    data: bytes = obj["Body"].read()
    return data