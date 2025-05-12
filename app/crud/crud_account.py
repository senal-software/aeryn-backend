# app/crud/crud_account.py
from typing import Optional
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate
# You might need a password hashing utility here
# from app.core.security import get_password_hash # Example

class CRUDAccount(CRUDBase[Account, AccountCreate, AccountUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Account]:
        return db.query(Account).filter(Account.email == email).first()

    def create(self, db: Session, *, obj_in: AccountCreate) -> Account:
        create_data = obj_in.model_dump()
        print("WARNING: Storing plain password - HASH in production!")
        db_obj = Account(**create_data) # Make sure Account model matches AccountCreate fields 

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Account, obj_in: AccountUpdate
    ) -> Account:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    # Add other specific account methods if needed

account = CRUDAccount(Account)