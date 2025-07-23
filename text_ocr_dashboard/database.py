import sqlite3
from datetime import datetime

DB_NAME = "ocr_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ocr_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            text TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_entry(filename, text):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ocr_log (filename, text, timestamp) VALUES (?, ?, ?)",
                   (filename, text, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def fetch_recent_entries(limit=10):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT filename, timestamp FROM ocr_log ORDER BY timestamp DESC LIMIT ?", (limit,))
    result = cursor.fetchall()
    conn.close()
    return result
