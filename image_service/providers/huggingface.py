import httpx

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

    async def generate(self, prompt: str, **kwargs):
        """
        Hugging Face provider.
        HTTP request will be added in the next step.
        """

        return {
            "success": False,
            "provider": self.name,
            "model": self.model,
            "image_url": None,
            "error": "HTTP request not implemented yet."
        }
