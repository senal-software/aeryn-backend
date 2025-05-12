# app/schemas/account.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Shared properties
class AccountBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

# Properties to receive via API on creation
class AccountCreate(AccountBase):
    pass

# Properties to receive via API on update
class AccountUpdate(AccountBase):
    email: Optional[EmailStr] = None # Allow updating email
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

# Properties stored in DB (without password)
class AccountInDBBase(AccountBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    # Pydantic V2 configuration: allows reading data from ORM models
    model_config = {
        "from_attributes": True
    }

# Properties to return to client
class Account(AccountInDBBase):
    pass

# Properties stored in DB
class AccountInDB(AccountInDBBase):
    hashed_password: str