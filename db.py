"""PostgreSQL storage for the application."""

import os

import psycopg2


def get_connection():
    """Open a connection using PostgreSQL's standard PG* environment variables."""
    return psycopg2.connect(
        dbname=os.getenv("PGDATABASE", "ara_flet"),
        user=os.getenv("PGUSER", "postgres"),
        # Matches the local PostgreSQL password already used by this project.
        # Set PGPASSWORD to override it on another machine.
        password=os.getenv("PGPASSWORD") or "12345",
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
    )


def init_db():
    """Create the users table if it does not already exist."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )


def add_user(name, age, email, password):
    """Insert a new user. Returns (success: bool, message: str)."""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (name, age, email, password) VALUES (%s, %s, %s, %s)",
                    (name, age, email, password),
                )
        return True, "Account created successfully."
    except psycopg2.errors.UniqueViolation:
        return False, "That email is already registered."


def get_user_by_email(email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cur.fetchone()


def verify_login(email, password):
    """Return the user row if email/password match, else None."""
    row = get_user_by_email(email)
    if row and row[4] == password:
        return row
    return None


def get_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, age, email, password, created_at FROM users ORDER BY id DESC"
            )
            return cur.fetchall()


def delete_user(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))


def count_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM users")
            return cur.fetchone()[0]
