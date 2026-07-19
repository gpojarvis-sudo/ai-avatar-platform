from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from video_service.service import video_service

router = APIRouter(
    prefix="/video",
    tags=["Video Generation"],
)


class VideoRequest(BaseModel):
    image_path: str
    audio_path: str
    avatar_path: str = ""
    provider: str = "ffmpeg"
    extension: str = "mp4"


@router.post("/generate")
async def generate_video(request: VideoRequest):
    try:
        result = await video_service.generate(
            image_path=request.image_path,
            audio_path=request.audio_path,
            avatar_path=request.avatar_path,
            provider=request.provider,
            extension=request.extension,
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
