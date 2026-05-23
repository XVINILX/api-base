from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from core.database.main import Base


class User(Base):
    __tablename__ = "users"
    
    uuid = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<User {self.username}>"