"""
Auth: login and register. User data stored in PostgreSQL.
Pre-seeded demo user: demo@community.ai / password123
"""
import hashlib
import secrets

import psycopg2
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.db.postgres import create_user, get_user_by_email

router = APIRouter(prefix="/auth", tags=["auth"])


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


class LoginBody(BaseModel):
    email: str
    password: str


class RegisterBody(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(body: LoginBody):
    """Validate credentials against PostgreSQL and return email + token."""
    email = body.email.strip().lower()
    if not email:
        raise HTTPException(status_code=400, detail="Email required")
    user = get_user_by_email(email)
    if not user or user["password_hash"] != _hash_password(body.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = secrets.token_urlsafe(32)
    return {"email": email, "token": token}


@router.post("/register")
def register(body: RegisterBody):
    """Create a new user in PostgreSQL. Email must be unique."""
    email = body.email.strip().lower()
    if not email:
        raise HTTPException(status_code=400, detail="Email required")
    password_hash = _hash_password(body.password)
    try:
        create_user(email, password_hash)
    except psycopg2.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"email": email}
