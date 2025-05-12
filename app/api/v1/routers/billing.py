
from fastapi import APIRouter


router = APIRouter(
    prefix="/billing",
    tags=["billing"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)


@router.get("/packages")
async def get_packages():
    return {
        "packages": [],
    }


