import csv
import sqlite3

from collections import Counter

DATABASE_FILE = "security_logs.db"
CSV_FILE = "login_events.csv"
FAILURE_ATTEMPTS = 3


def create_database(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS login_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            username TEXT NOT NULL,
            ip_adress TEXT NOT NULL,
            status TEXT NOT NULL
        )
        """
    )
    connection.commit()


def import_events(connection: sqlite3.Connection) -> None:
    with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            connection.execute(
                """
                INSERT INTO login_events
                (timestamp, username, ip_address, status)
                VALUES (?, ?, ?, ?)
                """,
                (
                    row["timestamp"],
                    row["username"],
                    row["ip_address"],
                    row["status"],
                ),
            )

    connection.commit()