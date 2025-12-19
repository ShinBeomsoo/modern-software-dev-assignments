from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, List, Optional


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "app.db"


@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    """
    Context manager for SQLite connections. ensures the data directory exists
    and the connection is closed properly.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def init_db() -> None:
    """Initialize the database schema."""
    with get_db_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS action_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                note_id INTEGER,
                text TEXT NOT NULL,
                done INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (note_id) REFERENCES notes(id)
            );
        """)
        conn.commit()


def insert_note(content: str) -> int:
    with get_db_connection() as conn:
        cursor = conn.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        conn.commit()
        return int(cursor.lastrowid)


def get_note(note_id: int) -> Optional[sqlite3.Row]:
    with get_db_connection() as conn:
        return conn.execute(
            "SELECT id, content, created_at FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()


def list_notes() -> List[sqlite3.Row]:
    with get_db_connection() as conn:
        return list(conn.execute("SELECT id, content, created_at FROM notes ORDER BY id DESC").fetchall())


def insert_action_items(items: List[str], note_id: Optional[int] = None) -> List[int]:
    ids: List[int] = []
    with get_db_connection() as conn:
        for item in items:
            cursor = conn.execute(
                "INSERT INTO action_items (note_id, text) VALUES (?, ?)",
                (note_id, item),
            )
            ids.append(int(cursor.lastrowid))
        conn.commit()
    return ids


def list_action_items(note_id: Optional[int] = None) -> List[sqlite3.Row]:
    query = "SELECT id, note_id, text, done, created_at FROM action_items"
    params = []
    if note_id is not None:
        query += " WHERE note_id = ?"
        params.append(note_id)
    query += " ORDER BY id DESC"

    with get_db_connection() as conn:
        return list(conn.execute(query, params).fetchall())


def mark_action_item_done(action_item_id: int, done: bool) -> bool:
    """Updates the done status. Returns True if successfully updated."""
    with get_db_connection() as conn:
        cursor = conn.execute(
            "UPDATE action_items SET done = ? WHERE id = ?",
            (1 if done else 0, action_item_id),
        )
        conn.commit()
        return cursor.rowcount > 0


