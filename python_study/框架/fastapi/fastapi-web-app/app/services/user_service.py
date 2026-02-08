"""
User service layer
"""
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.security import get_password_hash, verify_password


class UserService:
    """User service class"""
    
    @staticmethod
    def get_user(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_users(
        db: Session, skip: int = 0, limit: int = 100
    ) -> List[User]:
        """Get list of users with pagination"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_user(db: Session, user_in: UserCreate) -> User:
        """Create new user"""
        # Check if user already exists
        if UserService.get_user_by_email(db, user_in.email):
            raise ValueError("User with this email already exists")
        if UserService.get_user_by_username(db, user_in.username):
            raise ValueError("User with this username already exists")
        
        # Create user
        db_user = User(
            email=user_in.email,
            username=user_in.username,
            full_name=user_in.full_name,
            hashed_password=get_password_hash(user_in.password),
            is_active=user_in.is_active,
            is_superuser=user_in.is_superuser,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def update_user(
        db: Session, user_id: int, user_in: UserUpdate
    ) -> Optional[User]:
        """Update user"""
        db_user = UserService.get_user(db, user_id)
        if not db_user:
            return None
        
        # Update fields
        update_data = user_in.dict(exclude_unset=True)
        
        # Handle password update
        if "password" in update_data:
            hashed_password = get_password_hash(update_data.pop("password"))
            update_data["hashed_password"] = hashed_password
        
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Delete user"""
        db_user = UserService.get_user(db, user_id)
        if not db_user:
            return False
        
        db.delete(db_user)
        db.commit()
        return True
    
    @staticmethod
    def authenticate_user(
        db: Session, username: str, password: str
    ) -> Optional[User]:
        """Authenticate user"""
        user = UserService.get_user_by_username(db, username)
        if not user:
            # Try email
            user = UserService.get_user_by_email(db, username)
        
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user