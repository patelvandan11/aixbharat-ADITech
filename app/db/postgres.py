"""
PostgreSQL connection and users table for auth.
Set DATABASE_URL in .env (e.g. postgresql://user:password@host:5432/dbname).
"""
import hashlib
from contextlib import contextmanager
from typing import Optional

import psycopg2

from psycopg2.extras import RealDictCursor

from app.core.config import DATABASE_URL

USERS_TABLE = "users"


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


@contextmanager
def get_connection():
    """Yield a DB connection with RealDictCursor. Closes on exit."""
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_users_table():
    """
    Create users table if not exists and seed demo user (demo@community.ai / password123).
    Safe to call on every startup or first request.
    """
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password_hash VARCHAR(64) NOT NULL,
                    created_at TIMESTAMPTZ DEFAULT NOW()
                )
                """
            )
            # Seed demo user if missing
            demo_email = "demo@community.ai"
            demo_hash = _hash_password("password123")
            cur.execute(
                """
                INSERT INTO users (email, password_hash)
                VALUES (%s, %s)
                ON CONFLICT (email) DO NOTHING
                """,
                (demo_email, demo_hash),
            )


def get_user_by_email(email: str) -> Optional[dict]:
    """Return user row (with password_hash) or None."""
    init_users_table()
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "SELECT id, email, password_hash, created_at FROM users WHERE email = %s",
                (email.lower(),),
            )
            row = cur.fetchone()
            return dict(row) if row else None


def create_user(email: str, password_hash: str) -> None:
    """Insert a new user. Caller must handle IntegrityError for duplicate email."""
    init_users_table()
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (email, password_hash) VALUES (%s, %s)",
                (email.lower(), password_hash),
            )
