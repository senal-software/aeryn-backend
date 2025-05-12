# app/models/account.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.db.session import Base # Import Base from the central location

class Account(Base):
    __tablename__ = "accounts" # Table name in the database

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
