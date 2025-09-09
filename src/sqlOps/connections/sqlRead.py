# add parent directory to system paths
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from sqlOps.sqlConn import get_conn

def sqlGetConnections(userID : str):
    conn = get_conn()
    ra = []
    with conn.cursor() as cur:
        cur.execute("""SELECT user2 FROM connections
                    WHERE user1 = %s;""",
                    (userID,))
        for res in cur.fetchall():
            for friend in res:
                ra.append(friend)

        # second sweep through
        cur.execute("""SELECT user1 FROM connections
                    WHERE user2 = %s;""",
                    (userID,))
        for res in cur.fetchall():
            for friend in res:
                ra.append(friend)
        return ra