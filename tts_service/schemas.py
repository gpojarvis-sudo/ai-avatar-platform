from typing import Optional

from pydantic import BaseModel, Field


class TTSRequest(BaseModel):
    """
    Standard request model for all TTS providers.
    """

    text: str = Field(
        ...,
        min_length=1,
        description="Text to convert into speech."
    )

    voice: str = Field(
        default="default",
        description="Voice name or provider-specific voice ID."
    )

    language: str = Field(
        default="hi-IN",
        description="Language code."
    )

    speed: float = Field(
        default=1.0,
        ge=0.5,
        le=2.0,
        description="Speech speed multiplier."
    )

    provider: Optional[str] = Field(
        default=None,
        description="Optional provider override."
    )


class TTSResponse(BaseModel):
    """
    Standard response returned by every provider.
    """

    success: bool

    provider: str

    voice: str

    language: str

    filename: str

    audio_url: str

    message: Optional[str] = None
