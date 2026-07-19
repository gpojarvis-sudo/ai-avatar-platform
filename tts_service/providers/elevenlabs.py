import os
import uuid
from pathlib import Path

import httpx

from tts_service.providers.base import BaseTTSProvider
from tts_service.schemas import TTSRequest, TTSResponse


class ElevenLabsProvider(BaseTTSProvider):

    @property
    def name(self) -> str:
        return "elevenlabs"

    async def generate(
        self,
        request: TTSRequest,
    ) -> TTSResponse:

        api_key = os.getenv("ELEVENLABS_API_KEY")

        if not api_key:
            raise ValueError(
                "ELEVENLABS_API_KEY is not configured."
            )

        voice = (
            request.voice
            if request.voice != "default"
            else os.getenv(
                "ELEVENLABS_DEFAULT_VOICE",
                "CwhRBWXzGAHq8TQ4Fs17",
            )
        )

        payload = {
            "text": request.text,
            "model_id": os.getenv(
                "ELEVENLABS_MODEL",
                "eleven_multilingual_v2",
            )
        }

        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
                headers=headers,
                json=payload,
            )

        response.raise_for_status()

        audio_dir = Path("static/audio")
        audio_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{uuid.uuid4().hex}.mp3"

        filepath = audio_dir / filename

        filepath.write_bytes(response.content)

        return TTSResponse(
            success=True,
            provider=self.name,
            voice=voice,
            language=request.language,
            filename=filename,
            audio_url=f"/static/audio/{filename}",
            message="Speech generated successfully.",
        )
