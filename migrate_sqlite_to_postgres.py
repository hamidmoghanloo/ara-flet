"""Copy users from users.db to the configured PostgreSQL database."""

import os
import sqlite3

from db import get_connection, init_db


SQLITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")


def migrate():
    if not os.path.exists(SQLITE_PATH):
        raise FileNotFoundError(f"SQLite source database not found: {SQLITE_PATH}")

    with sqlite3.connect(SQLITE_PATH) as source:
        rows = source.execute(
            "SELECT id, name, age, email, password, created_at FROM users ORDER BY id"
        ).fetchall()

    init_db()
    inserted = 0
    skipped = 0
    with get_connection() as target:
        with target.cursor() as cur:
            for row in rows:
                cur.execute(
                    """
                    INSERT INTO users (id, name, age, email, password, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING
                    """,
                    row,
                )
                if cur.rowcount:
                    inserted += 1
                else:
                    skipped += 1

            cur.execute(
                """
                SELECT setval(
                    pg_get_serial_sequence('users', 'id'),
                    GREATEST(COALESCE((SELECT MAX(id) FROM users), 1), 1),
                    EXISTS (SELECT 1 FROM users)
                )
                """
            )

    print(f"Migration complete: {inserted} inserted, {skipped} already present.")


if __name__ == "__main__":
    migrate()
