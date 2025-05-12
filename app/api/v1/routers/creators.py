
from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/creators",
    tags=["creators"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)


@router.get("/feed")
async def get_creator_feed():
    return {
        "feed": [],
    }

@router.get("/{creator_id}")
async def get_creator(creator_id: int):
    return {
        "creator_id": creator_id,
    }


@router.post("/{creator_id}/process-image")
async def process_image(creator_id: int, image: UploadFile = File(...)):
    return {
        "creator_id": creator_id,
        "pages": [],
    }
