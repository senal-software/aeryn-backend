
from fastapi import APIRouter


router = APIRouter(
    prefix="/rewards",
    tags=["rewards"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)

@router.get("/daily/status")
async def get_daily_reward_status(user_id: int):
    return {
        "isAvailable": True,
        "nextAvailableTimestamp": "2021-01-01T00:00:00Z"
    }

@router.post("/daily/claim")
async def claim_daily_reward(user_id: int):
    return {
        "success": True,
        "coinsAwarded": 100,
        "newBalance": 1100,
    }
