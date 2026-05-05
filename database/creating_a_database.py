import sqlite3

# connect to database (creates file if not exists)
conn = sqlite3.connect("pacman.db")
cursor = conn.cursor()

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT DEFAULT CURRENT_TIMESTAMP,
    ended_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    player_name TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    lives INTEGER DEFAULT 3,
    FOREIGN KEY (game_id) REFERENCES games(id)
)
""")

# save changes
conn.commit()
conn.close()