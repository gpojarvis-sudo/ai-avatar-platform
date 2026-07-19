from pathlib import Path

from shared.logger import logger
from shared.utils import ensure_directory, generate_filename
from shared.constants import SUPPORTED_AUDIO_FORMATS


class TTSService:
    """
    Basic Text-to-Speech Service (MVP)

    Currently returns metadata only.
    Real Gemini / ElevenLabs / NVIDIA integration
    will be added later.
    """

    def __init__(self):
        self.output_dir = ensure_directory("static/audio")

    async def generate(
        self,
        text: str,
        voice: str = "default",
        provider: str = "gemini",
        extension: str = "mp3",
    ):

        if extension.lower() not in SUPPORTED_AUDIO_FORMATS:
            raise ValueError(
                f"Unsupported audio format: {extension}"
            )

        filename = generate_filename(
            extension=extension,
            prefix="tts",
        )

        output_path = Path(self.output_dir) / filename

        logger.info(
            f"TTS requested using '{provider}'"
        )

        logger.info(f"Voice : {voice}")
        logger.info(f"Text : {text}")

        return {
            "success": True,
            "provider": provider,
            "voice": voice,
            "text": text,
            "filename": filename,
            "output_path": str(output_path),
            "message": (
                "TTS provider integration "
                "will be added in the next step."
            ),
        }


tts_service = TTSService()
