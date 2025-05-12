
from fastapi import APIRouter


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
