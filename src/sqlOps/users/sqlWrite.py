# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from sqlOps.sqlConn import get_conn

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from lib.models import ProfileType

from fastapi import HTTPException
from psycopg import sql

def sqlCreateAccount(usr : ProfileType):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (userID, username, password, birthday, email, follows)
            VALUES (%s, %s, %s, (%s, %s, %s), %s, %s);""",
            (usr.userID, usr.username, usr.password, usr.birthday.day, usr.birthday.month, usr.birthday.year, usr.email, usr.follows,)
        )
        conn.commit()


def sqlRemoveAccount(userID : str):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM users
            WHERE userID = %s;""",
            (userID,)
        )
        conn.commit()

def sqlPatchAccount(userID : str, attribute: str, value: str):
    conn = get_conn()
    with conn.cursor() as cur:
        query = sql.SQL(
            "UPDATE users SET {col} = %s "
            "WHERE userID = %s "
            "RETURNING {col};"
        ).format(col=sql.Identifier(attribute))

        cur.execute( query, (value, userID,) )

        if value == cur.fetchone()[0]:
            conn.commit()
            return
        else:
            raise HTTPException(status_code=404, detail="User not found.")