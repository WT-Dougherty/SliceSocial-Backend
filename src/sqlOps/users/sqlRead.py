# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from sqlOps.sqlConn import get_conn

def sqlCheckID(id):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE userID = %s);", (id,))
        return cur.fetchone()[0]

def sqlCheckUsername(username):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE username = %s);", (username,))
        return cur.fetchone()[0]

def sqlCheckEmail(email):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE email = %s);", (email,))
        return cur.fetchone()[0]

def sqlAuthenticate(username, password):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT userID FROM users
                    WHERE username = %s AND password = %s;""",
                    (username, password,))
        result = cur.fetchone()
        if result:
            return result[0]
        else:
            return None

def sqlGetUserInfo(userID):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM users
                    WHERE userID = %s;""",
                    (userID,))
        return cur.fetchall()