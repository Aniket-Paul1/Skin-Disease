import sqlite3
import os
from datetime import datetime
import bcrypt

# Database file (stored in streamlit_app folder)
DB_PATH = os.path.join(os.path.dirname(__file__), "predictions.db")


# ------------------------------
# Database Initialization
# ------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL,
            city TEXT,
            state TEXT,
            created_at TEXT
        )
    """)

    # Predictions table (linked to users)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            disease TEXT,
            confidence REAL,
            source TEXT,
            timestamp TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


# ------------------------------
# User Authentication
# ------------------------------
def register_user(username, email, password, city, state):
    init_db()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute("""
            INSERT INTO users (username, email, password_hash, city, state, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (username, email, password_hash, city, state, datetime.now().isoformat()))

        conn.commit()
        return True, None

    except sqlite3.IntegrityError:
        return False, "Username or Email already exists"

    finally:
        conn.close()


def authenticate_user(username, password):
    init_db()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, password_hash, city, state
        FROM users WHERE username = ?
    """, (username,))

    row = cursor.fetchone()
    conn.close()

    if row and bcrypt.checkpw(password.encode(), row[2]):
        return {
            "id": row[0],
            "username": row[1],
            "city": row[3],
            "state": row[4]
        }

    return None


# ------------------------------
# Prediction Storage
# ------------------------------
def save_prediction(user_id, disease, confidence, source):
    init_db()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (user_id, disease, confidence, source, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, disease, confidence, source, datetime.now().isoformat()))

    conn.commit()
    conn.close()


# ------------------------------
# Fetch User Prediction History
# ------------------------------
def get_user_predictions(user_id):
    init_db()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT disease, confidence, source, timestamp
        FROM predictions
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows
