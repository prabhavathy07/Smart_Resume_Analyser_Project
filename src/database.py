import sqlite3


def create_database():
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    print("Creating tables...")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        job_role TEXT,
        score INTEGER,
        ats INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()

    print("Tables Created Successfully")

    conn.close()

def save_history(user_id, job_role, score, ats):
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    print("Saving to DB:", user_id, job_role, score, ats)

    cursor.execute(
        "INSERT INTO history(user_id, job_role, score, ats) VALUES (?, ?, ?, ?)",
        (user_id, job_role, score, ats)
    )

    conn.commit()

    print("History Saved Successfully!")

    conn.close()


def get_history(user_id):
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM history WHERE user_id=? ORDER BY id DESC",
        (user_id,)
    )

    data = cursor.fetchall()

    conn.close()

    return data

def create_user(name, email, password):
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login_user(email):
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    return user