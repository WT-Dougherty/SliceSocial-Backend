from .sqlConn import get_conn

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