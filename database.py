import sqlite3

def init_db():
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            bot_response TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_log(user_input, bot_response, timestamp):
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("INSERT INTO chat_logs (user_input, bot_response, timestamp) VALUES (?, ?, ?)",
              (user_input, bot_response, timestamp))
    conn.commit()
    conn.close()
