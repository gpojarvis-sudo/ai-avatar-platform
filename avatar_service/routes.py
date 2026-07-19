from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from avatar_service.service import avatar_service

router = APIRouter(
    prefix="/avatar",
    tags=["Avatar Generation"],
)


class AvatarRequest(BaseModel):
    image_path: str
    audio_path: str
    provider: str = "sadtalker"
    extension: str = "mp4"


@router.post("/generate")
async def generate_avatar(request: AvatarRequest):
    try:
        result = await avatar_service.generate(
            image_path=request.image_path,
            audio_path=request.audio_path,
            provider=request.provider,
            extension=request.extension,
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
