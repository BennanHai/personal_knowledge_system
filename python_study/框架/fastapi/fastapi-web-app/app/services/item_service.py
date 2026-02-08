"""
Item service layer
"""
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class ItemService:
    """Item service class"""
    
    @staticmethod
    def get_item(db: Session, item_id: int) -> Optional[Item]:
        """Get item by ID"""
        return db.query(Item).filter(Item.id == item_id).first()
    
    @staticmethod
    def get_items(
        db: Session, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        """Get list of items with pagination"""
        return db.query(Item).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_items_by_owner(
        db: Session, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Item]:
        """Get items by owner ID"""
        return (
            db.query(Item)
            .filter(Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    @staticmethod
    def create_item(db: Session, item_in: ItemCreate, owner_id: int) -> Item:
        """Create new item"""
        db_item = Item(
            **item_in.dict(exclude={"owner_id"}),
            owner_id=owner_id,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def update_item(
        db: Session, item_id: int, item_in: ItemUpdate
    ) -> Optional[Item]:
        """Update item"""
        db_item = ItemService.get_item(db, item_id)
        if not db_item:
            return None
        
        # Update fields
        update_data = item_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_item, field, value)
        
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def delete_item(db: Session, item_id: int) -> bool:
        """Delete item"""
        db_item = ItemService.get_item(db, item_id)
        if not db_item:
            return False
        
        db.delete(db_item)
        db.commit()
        return True