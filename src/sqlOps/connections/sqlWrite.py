# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from sqlOps.sqlConn import get_conn

def sqlAddConnection(user1 : str, user2: str):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO connections (user1, user2)
            VALUES (%s, %s);""",
            (user1, user2,)
        )
        conn.commit()