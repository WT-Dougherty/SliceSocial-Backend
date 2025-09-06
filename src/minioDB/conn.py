import boto3
from botocore.config import Config
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
PASSWORD = os.getenv('MINIO_PASSWORD')
URL = os.getenv("MINIO_URL")

s3 = boto3.client(
    "s3",
    endpoint_url=URL,   # change to https:// for TLS
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=PASSWORD,
)