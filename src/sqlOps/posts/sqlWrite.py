# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from datetime import datetime
from dateutil import parser

from sqlOps.sqlConn import get_conn
from lib.models import PostType

def sqlAddPost(post : PostType):
    conn = get_conn()
    dt : datetime = parser.isoparse(post.posted_at)
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO posts (postID, userID, username, posted_at)
            VALUES (%s, %s, %s, %s);""",
            (post.postID, post.userID, post.username, dt,)
        )
        conn.commit()

def sqlRemovePost(postID : str):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            """
            DELETE FROM posts
            WHERE postID = %s;""",
            (postID,)
        )
        conn.commit()