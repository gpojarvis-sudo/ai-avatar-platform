import httpx
from pathlib import Path
from typing import Any, Dict

from config.settings import settings
from .base import BaseImageProvider


class HuggingFaceProvider(BaseImageProvider):
    """
    Hugging Face Image Generation Provider
    """

    name = "huggingface"

    def __init__(self):
        self.api_key = settings.HUGGINGFACE_API_KEY
        self.base_url = settings.HUGGINGFACE_BASE_URL
        self.model = settings.HUGGINGFACE_MODEL
        self.timeout = settings.HUGGINGFACE_TIMEOUT

        self.image_dir = Path("static/images")
        self.image_dir.mkdir(parents=True, exist_ok=True)

    async def generate(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """
        Generate image using Hugging Face.
        (HTTP integration will be added later.)
        """

        if not self.api_key:
            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "image_url": None,
                "error": "Hugging Face API key is not configured."
            }

        return {
            "success": False,
            "provider": self.name,
            "model": self.model,
            "image_url": None,
            "error": "HTTP request not implemented yet."
        }
