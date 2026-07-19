from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from image_service.service import image_service

router = APIRouter(
    prefix="/image",
    tags=["Image Generation"],
)


class ImageRequest(BaseModel):
    prompt: str
    provider: str = "gemini"
    extension: str = "png"


@router.post("/generate")
async def generate_image(request: ImageRequest):
    try:
        result = await image_service.generate(
            prompt=request.prompt,
            provider=request.provider,
            extension=request.extension,
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
