from fastapi import APIRouter
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas # Use __init__ imports
from app import crud    # Use __init__ imports
from app import models  # Use __init__ imports (optional here if only using crud)
from app.dependencies import get_db # Import the dependency

router = APIRouter(
    prefix="/account",
    tags=["account"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)


@router.get("/balance")
async def get_balance(user_id: int):
    return {
        "user_id": user_id,
        "balance": 1000,
    }

@router.get("/transactions")
async def get_transactions(user_id: int):
    return {
        "user_id": user_id,
        "transactions": [],
    }

@router.get("/{account_id}", response_model=schemas.Account)
def read_account(
    *,
    db: Session = Depends(get_db),
    account_id: int,
) -> Any:
    """
    Get account by ID.
    """
    account = crud.account.get(db=db, id=account_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )
    return account

@router.get("/", response_model=List[schemas.Account])
def read_accounts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve accounts.
    """
    accounts = crud.account.get_multi(db, skip=skip, limit=limit)
    return accounts

@router.put("/{account_id}", response_model=schemas.Account)
def update_account(
    *,
    db: Session = Depends(get_db),
    account_id: int,
    account_in: schemas.AccountUpdate,
) -> Any:
    """
    Update an account.
    """
    account = crud.account.get(db=db, id=account_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )
    account = crud.account.update(db=db, db_obj=account, obj_in=account_in)
    return account

@router.delete("/{account_id}", response_model=schemas.Account)
def delete_account(
    *,
    db: Session = Depends(get_db),
    account_id: int,
) -> Any:
    """
    Delete an account.
    """
    account = crud.account.get(db=db, id=account_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found",
        )
    deleted_account = crud.account.remove(db=db, id=account_id)
    return deleted_account