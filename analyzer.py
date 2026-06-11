import csv
import sqlite3

from collections import Counter

DATABASE_FILE = "security_logs.db"
CSV_FILE = "login_events.csv"
FAILURE_ATTEMPTS = 3

