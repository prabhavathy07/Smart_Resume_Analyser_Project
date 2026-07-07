import sqlite3


def create_database():
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_role TEXT,
            score INTEGER,
            ats INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save_history(job_role, score, ats):
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history(job_role, score, ats) VALUES (?, ?, ?)",
        (job_role, score, ats)
    )

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect("resume_history.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")

    data = cursor.fetchall()

    conn.close()

    return data