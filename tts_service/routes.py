from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from tts_service.service import tts_service

router = APIRouter(
    prefix="/tts",
    tags=["Text To Speech"],
)


class TTSRequest(BaseModel):
    text: str
    voice: str = "default"
    provider: str = "gemini"
    extension: str = "mp3"


@router.post("/generate")
async def generate_tts(request: TTSRequest):
    try:
        result = await tts_service.generate(
            text=request.text,
            voice=request.voice,
            provider=request.provider,
            extension=request.extension,
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
