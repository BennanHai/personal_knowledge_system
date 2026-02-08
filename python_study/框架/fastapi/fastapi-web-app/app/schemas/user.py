"""
User Pydantic models
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, validator


# Base schemas
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


# Create schemas
class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str
    
    @validator("password")
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return v


class UserUpdate(UserBase):
    password: Optional[str] = None


# Response schemas
class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class User(UserInDBBase):
    """User response schema (without password)"""
    pass


class UserInDB(UserInDBBase):
    """User in database schema (with password)"""
    hashed_password: str