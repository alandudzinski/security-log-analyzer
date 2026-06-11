import csv
import sqlite3

from collections import Counter

DATABASE_FILE = "security_logs.db"
CSV_FILE = "login_events.csv"
FAILURE_ATTEMPTS = 3 # Threshold for determining if an IP is suspicious


# Create the login_events database
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


# Import events from the included login_events.csv into db
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


# Extract any suspicious ip addresses from the login events
def detect_suspicious_ips(connection: sqlite3.Connection) -> None:
    rows = connection.execute(
        """
        SELECT ip_address FROM login_events
        WHERE status = 'failed'
        """
    ).fetchall()

    failed_attempts = Counter(row[0] for row in rows)

    print("\nSuspicious IP addresses:")

    found = False

    # Finds all IP addresses with many failed attempts
    for ip_address, count in failed_attempts.items():
        if count >= FAILURE_ATTEMPTS:
            print(f"- {ip_address}: {count} failed attempts")
            found = True

    if not found:
        print("No suspicious IP addresses detected.")


def main() -> None:
    try:
        with sqlite3.connect(DATABASE_FILE) as connection:
            create_database(connection)
            import_events(connection)
            detect_suspicious_ips(connection)
    # Credits to ChatGPT for pointing out I should use try/except blocks here
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} was not found.")
    except (sqlite3.Error, KeyError) as error:
        print(f"Error: {error}")


# Ensure this script is not called outside running main
if __name__ == "__main__":
    main()