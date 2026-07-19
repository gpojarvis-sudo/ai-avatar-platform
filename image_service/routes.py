from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from image_service.service import ImageService

router = APIRouter(
    prefix="/image",
    tags=["Image Generation"],
)

service = ImageService()


class ImageRequest(BaseModel):

    prompt: str = Field(
        ...,
        min_length=5,
        max_length=5000,
        description="Image prompt",
    )

    negative_prompt: str = Field(
        default="",
        max_length=2000,
        description="Negative prompt",
    )

    aspect_ratio: str = Field(
        default="1:1",
        description="1:1 | 9:16 | 16:9 | 4:5 | 3:2",
    )

    quality: str = Field(
        default="balanced",
        description="fast | balanced | ultra",
    )

    seed: int | None = Field(
        default=None,
        description="Optional random seed",
    )

    provider: str = Field(
        default="cloudflare",
        description="cloudflare | huggingface | gemini | nvidia",
    )

    model: str = Field(
        default="pruna/p-image",
        description="Cloudflare Workers AI model",
    )

    extension: str = Field(
        default="png",
        description="png | jpg | jpeg | webp",
    )


@router.post("/generate")
async def generate_image(request: ImageRequest):

    try:

        result = await service.generate(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            aspect_ratio=request.aspect_ratio,
            quality=request.quality,
            seed=request.seed,
            provider=request.provider,
            model=request.model,
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
