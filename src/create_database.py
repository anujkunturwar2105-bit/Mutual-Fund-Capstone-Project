"""
Create the Bluestock Mutual Fund SQLite database.

This module creates the SQLite database file and initializes
the required database structure.
"""

import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "bluestock_mf.db"


def create_database():
    """Create the SQLite database and initialize the schema."""

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.cursor()

        # Create database metadata table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS database_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        connection.commit()

    finally:
        connection.close()

    print(f"Database ready: {DATABASE_PATH}")


if __name__ == "__main__":
    create_database()