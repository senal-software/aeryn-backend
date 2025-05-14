# app/schemas/account.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Shared properties
class AccountBase(BaseModel):
    email: EmailStr
    coin_balance: int

# Properties to receive via API on creation
class AccountCreate(AccountBase):
    pass

# Properties to receive via API on update
class AccountUpdate(AccountBase):
    email: Optional[EmailStr] = None # Allow updating email
    coin_balance: Optional[int] = None

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
    pass