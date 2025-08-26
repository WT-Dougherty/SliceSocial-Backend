import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USERS_READ = os.getenv('DB_USERS_READ')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

def sqlCheckID(id):
    with psycopg.connect(
        dbname=DB_NAME,
        user='postgres',
        password=DB_PASSWORD,
        host=DB_USERS_READ,
        port=DB_PORT
        ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE userID = %s);", (id,))
            return cur.fetchone()[0]