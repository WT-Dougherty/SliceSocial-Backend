# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from sqlOps.sqlConn import get_conn

def sqlGetPostComments(postID : str):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM comments
                    WHERE postID = %s;""",
                    (postID,))
        return cur.fetchall()