from .sqlConn import get_conn

def sqlViewTable():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        for row in cur.fetchall():
            print(row)