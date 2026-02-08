"""
Token Pydantic models
"""
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    """Token response schema"""
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Token payload schema"""
    sub: Optional[str] = None


class LoginRequest(BaseModel):
    """Login request schema"""
    username: str
    password: str