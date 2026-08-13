"""
Verify row counts for the Bluestock Mutual Fund database.

This script checks whether the expected database tables
contain records after the ETL process.
"""

import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent / "bluestock_mf.db"


def verify_row_counts():
    """Display row counts for all tables in the SQLite database."""

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            ORDER BY name
            """
        )

        tables = [row[0] for row in cursor.fetchall()]

        for table in tables:
            cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
            count = cursor.fetchone()[0]
            print(f"{table}: {count:,} rows")

    finally:
        connection.close()


if __name__ == "__main__":
    verify_row_counts()