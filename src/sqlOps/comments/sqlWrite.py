# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from datetime import datetime
from dateutil import parser

from lib.models import CommentType
from sqlOps.sqlConn import get_conn

def sqlAddComment(comment : CommentType):
    conn = get_conn()
    dt : datetime = parser.isoparse(comment.posted_at)
    print(dt)
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO comments (postID, commentID, username, comment, posted_at)
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    (comment.postID, comment.commentID, comment.username, comment.comment, dt,))
        conn.commit()