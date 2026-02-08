"""
Item Pydantic models
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


# Base schemas
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = True


# Create schemas
class ItemCreate(ItemBase):
    title: str
    owner_id: Optional[int] = None


class ItemUpdate(ItemBase):
    pass


# Response schemas
class ItemInDBBase(ItemBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class Item(ItemInDBBase):
    """Item response schema"""
    pass


class ItemInDB(ItemInDBBase):
    """Item in database schema"""
    pass