from .base import BaseImageProvider


class GeminiProvider(BaseImageProvider):
    """
    Gemini Image Generation Provider
    """

    name = "gemini"

    async def generate(self, prompt: str, **kwargs):
        """
        Temporary placeholder implementation.
        Actual Gemini integration will be added later.
        """

        return {
            "success": False,
            "provider": self.name,
            "image_url": None,
            "error": "Gemini provider is not configured yet."
        }
