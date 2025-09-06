# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from sqlOps.sqlConn import get_conn

def sqlGetPost(postID : str):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM posts
                    WHERE postID = %s;""",
                    (postID,))
        return cur.fetchall()

def sqlGetProfilePosts(userID : str):
    print(userID)
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM posts
                    WHERE userID = %s;""",
                    (userID,))
        return cur.fetchall()