
import os
import hashlib
import secrets
import hmac
from contextlib import contextmanager
import psycopg2
from psycopg2 import errors


# ==========================================
# 1. POSTGRESQL CONFIGURATION
# ==========================================

DB_CONFIG = {
    "host": os.getenv("DB_HOST", ""),
    "port": int(os.getenv("DB_PORT", "")),
    "dbname": os.getenv("DB_NAME", ""),
    "user": os.getenv("DB_USER", ""),
    "password": os.getenv("DB_PASSWORD", ""),
}


# ==========================================
# 2. DATABASE CONNECTION
# ==========================================

@contextmanager
def get_connection():

    conn = psycopg2.connect(**DB_CONFIG)

    try:
        yield conn
        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


# ==========================================
# 3. PASSWORD HASHING
# ==========================================

def hash_password(password):

    salt = secrets.token_hex(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        600000
    ).hex()

    return f"{salt}${hashed}"


def check_password(password, stored_hash):

    try:
        salt, original_hash = stored_hash.split("$")

        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            600000
        ).hex()

        return hmac.compare_digest(new_hash, original_hash)

    except (ValueError, AttributeError):
        return False


# ==========================================
# 4. INITIALIZE DATABASE
# ==========================================

def init_db():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (

                    id INTEGER GENERATED ALWAYS AS IDENTITY
                        PRIMARY KEY,

                    name VARCHAR(100) NOT NULL,

                    age INTEGER NOT NULL
                        CHECK (age BETWEEN 1 AND 120),

                    email VARCHAR(255) NOT NULL UNIQUE,

                    password_hash TEXT NOT NULL,

                    created_at TIMESTAMP
                        DEFAULT CURRENT_TIMESTAMP
                );
            """)

    print("Users table initialized successfully!")


# ==========================================
# 5. REGISTER USER
# ==========================================

def add_user(name, age, email, password):

    try:

        secure_password = hash_password(password)

        with get_connection() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO users
                    (name, age, email, password_hash)

                    VALUES (%s, %s, %s, %s);
                """, (
                    name.strip(),
                    int(age),
                    email.strip().lower(),
                    secure_password
                ))

        return True, "Account created successfully."

    except errors.UniqueViolation:
        return False, "This email is already registered."

    except (ValueError, TypeError):
        return False, "Invalid age."

    except psycopg2.Error as error:
        print("Database error:", error)
        return False, "Could not create account."


# ==========================================
# 6. FIND USER BY EMAIL
# ==========================================

def get_user_by_email(email):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    id,
                    name,
                    age,
                    email,
                    password_hash,
                    created_at

                FROM users

                WHERE email = %s;
            """, (email.strip().lower(),))

            user = cur.fetchone()

    return user


# ==========================================
# 7. LOGIN VERIFICATION
# ==========================================

def verify_login(email, password):

    user = get_user_by_email(email)

    if user and check_password(password, user[4]):
        return user

    return None


# ==========================================
# 8. GET ALL USERS FOR DASHBOARD
# ==========================================

def get_all_users():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    id,
                    name,
                    age,
                    email,
                    created_at

                FROM users

                ORDER BY id DESC;
            """)

            users = cur.fetchall()

    return users


# ==========================================
# 9. DELETE USER
# ==========================================

def delete_user(user_id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                DELETE FROM users
                WHERE id = %s;
            """, (user_id,))

            deleted = cur.rowcount

    return deleted > 0


# ==========================================
# 10. COUNT USERS
# ==========================================

def count_users():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT COUNT(*)
                FROM users;
            """)

            total = cur.fetchone()[0]

    return total


# ==========================================
# 11. TEST CONNECTION
# ==========================================

if __name__ == "__main__":

    try:
        init_db()

        print("PostgreSQL connected successfully!")
        print("Total registered users:", count_users())

    except psycopg2.Error as error:
        print("Database connection failed:", error)
