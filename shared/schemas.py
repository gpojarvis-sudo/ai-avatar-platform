from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


# ==========================================================
# Common API Response
# ==========================================================

class APIResponse(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Optional[Dict[str, Any]] = None


# ==========================================================
# Image Generation
# ==========================================================

class ImageGenerationRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    negative_prompt: Optional[str] = None
    width: int = 1024
    height: int = 1024
    provider: str = "gemini"


class ImageGenerationResponse(BaseModel):
    image_url: str
    provider: str


# ==========================================================
# Text-to-Speech
# ==========================================================

class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1)
    voice: str = "default"
    provider: str = "gemini"


class TTSResponse(BaseModel):
    audio_url: str
    provider: str


# ==========================================================
# Avatar Animation
# ==========================================================

class AvatarRequest(BaseModel):
    image_url: str
    audio_url: str
    provider: str = "local"


class AvatarResponse(BaseModel):
    video_url: str
    provider: str


# ==========================================================
# Video Generation
# ==========================================================

class VideoRequest(BaseModel):
    prompt: str
    provider: str = "veo"


class VideoResponse(BaseModel):
    video_url: str
    provider: str


# ==========================================================
# Health Check
# ==========================================================

class HealthResponse(BaseModel):
    status: str = "healthy"
    version: str
