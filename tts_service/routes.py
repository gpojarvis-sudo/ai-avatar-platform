from fastapi import APIRouter, HTTPException

from tts_service.schemas import (
    TTSRequest,
    TTSResponse,
)

from tts_service.service import tts_service


router = APIRouter(
    prefix="/tts",
    tags=["Text To Speech"],
)


@router.post(
    "/generate",
    response_model=TTSResponse,
)
async def generate_tts(
    request: TTSRequest,
):
    """
    Generate speech from text.
    """

    try:
        return await tts_service.generate(request)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get("/providers")
async def get_providers():
    """
    Get available TTS providers.
    """

    return {
        "providers": await tts_service.get_available_providers()
    }


@router.get("/health")
async def health():
    """
    Get health status of all providers.
    """

    return await tts_service.health()
