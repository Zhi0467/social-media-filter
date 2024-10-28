import sqlite3

DB_PATH = 'data/social_summarizer.db'

def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def get_user_preferences(username):
    """Fetch user preferences from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT preferences FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return eval(result[0]) if result else None  # Convert string back to list

def save_fetched_post(user_id, post_id, text, timestamp):
    """Save a fetched post to the database."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO posts (id, user_id, text, timestamp) VALUES (?, ?, ?, ?)",
            (post_id, user_id, text, timestamp)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Post {post_id} already exists.")
    conn.close()
