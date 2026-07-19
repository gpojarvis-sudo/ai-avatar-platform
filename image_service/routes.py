from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from image_service.service import image_service


router = APIRouter(
    prefix="/image",
    tags=["Image Generation"],
)


class ImageRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=3,
        description="Prompt for image generation",
    )

    provider: str = Field(
        default="huggingface",
        description="Image Provider",
    )

    extension: str = Field(
        default="png",
        description="Output Image Format",
    )


@router.post("/generate")
async def generate_image(
    request: ImageRequest,
):

    try:

        result = await image_service.generate(
            prompt=request.prompt,
            provider=request.provider,
            extension=request.extension,
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
