
from fastapi import APIRouter, Request


router = APIRouter(
    prefix="/webhooks",
    tags=["webhooks"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)


@router.post("/revenuecat")
async def revenuecat_webhook(request: Request):
    return {
        "success": True,
    }
