"""
Items API endpoints
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.services.item_service import ItemService
from app.api.v1.deps import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """Get list of items"""
    items = ItemService.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(
    item_in: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Create new item (authenticated)"""
    # Override owner_id with current user
    item_data = item_in.dict()
    item_data["owner_id"] = current_user.id
    item = ItemService.create_item(db, ItemCreate(**item_data), owner_id=current_user.id)
    return item


@router.get("/{item_id}", response_model=Item)
def read_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    """Get item by ID"""
    item = ItemService.get_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return item


@router.put("/{item_id}", response_model=Item)
def update_item(
    item_id: int,
    item_in: ItemUpdate,
    db: Session = Depends(get_db),
):
    """Update item"""
    item = ItemService.update_item(db, item_id, item_in)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    """Delete item"""
    success = ItemService.delete_item(db, item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
        )


@router.get("/owner/{owner_id}", response_model=List[Item])
def read_items_by_owner(
    owner_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """Get items by owner ID"""
    items = ItemService.get_items_by_owner(
        db, owner_id=owner_id, skip=skip, limit=limit
    )
    return items