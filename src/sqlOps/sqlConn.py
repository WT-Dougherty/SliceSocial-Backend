import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USERS_READ = os.getenv('DB_USERS_READ')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

_conn = None

def get_conn():
    global _conn
    if _conn is None:
        _conn = psycopg.connect(
            dbname=DB_NAME,
            user='postgres',
            password=DB_PASSWORD,
            host=DB_USERS_READ,
            port=DB_PORT,
            sslmode='require'
        )
    return _conn