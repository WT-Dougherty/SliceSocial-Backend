import os
import psycopg
from dotenv import load_dotenv

DB_USERS_READ = os.getenv('DB_USERS_READ')

def sqlCheckID(id):
    with psycopg.connect("dbname=slicePostgres user=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE id = %s);", (id,))
            return cur.fetchone()[0]