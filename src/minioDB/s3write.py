from .conn import s3
from fastapi import UploadFile
from fastapi import HTTPException, status

def s3add_post_image( file : UploadFile, postID : str ):
    try:
        s3.put_object(Bucket="post-images", Key=postID, Body=file.file)
        print( "File {} has been added".format(file.filename) )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File Upload Failed")

def s3add_profile_image( file : UploadFile, userID : str ):
    try:
        print("Filename is:", file)
        print("UserID is:", userID)
        s3.put_object(Bucket="profile-images", Key=userID, Body=file.file)
        print( "File {} has been added".format(file.filename) )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File Upload Failed")