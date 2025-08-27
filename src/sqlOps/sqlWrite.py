from .sqlConn import get_conn

import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from lib.models import ProfileType

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
            WHERE userID = %s""",
            (userID,)
        )
        conn.commit()


"""INSERT INTO users (userID, username, password, birthday, email, follows)
VALUES ('gh37xp0f7b5s98bh', 'WillDougherty', 'password', ('18', 'June', '2002'), 'willtdougherty@gmail.com', 0);"""