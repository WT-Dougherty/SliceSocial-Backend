# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from datetime import datetime

from lib.models import CommentType, GenerateTimestamp
from sqlOps.sqlConn import get_conn

def sqlAddComment(comment : CommentType):
    conn = get_conn()
    dt : datetime = GenerateTimestamp()
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO comments (postID, commentID, username, comment, posted_at)
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    (comment.postID, comment.commentID, comment.username, comment.comment, dt,))
        conn.commit()

def sqlRemoveComment(commentID : str):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM comments 
                    WHERE commentID = %s;
                    """,
                    (commentID,))
        conn.commit()