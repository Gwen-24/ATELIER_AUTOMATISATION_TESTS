# SQLite storage
import sqlite3
import json
from datetime import datetime

DB_NAME = "runs.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            api TEXT NOT NULL,
            passed INTEGER NOT NULL,
            failed INTEGER NOT NULL,
            total INTEGER NOT NULL,
            error_rate REAL NOT NULL,
            latency_avg REAL NOT NULL,
            latency_p95 REAL NOT NULL,
            tests_json TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_run(result):
    init_db()

    timestamp = datetime.now().isoformat(timespec="seconds")
    summary = result["summary"]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO runs (
            timestamp, api, passed, failed, total,
            error_rate, latency_avg, latency_p95, tests_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        result["api"],
        summary["passed"],
        summary["failed"],
        summary["total"],
        summary["error_rate"],
        summary["latency_ms_avg"],
        summary["latency_ms_p95"],
        json.dumps(result["tests"], ensure_ascii=False)
    ))

    conn.commit()
    conn.close()


def list_runs():
    init_db()

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM runs
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
