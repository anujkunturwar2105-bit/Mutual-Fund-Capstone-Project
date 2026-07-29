import sqlite3
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "bluestock_mf.db"

conn = sqlite3.connect(db_path)

print("Database created successfully!")

conn.close()