from .base import BaseImageProvider


class HuggingFaceProvider(BaseImageProvider):
    """
    Hugging Face Image Generation Provider
    """

    name = "huggingface"

    async def generate(self, prompt: str, **kwargs):
        """
        Temporary placeholder implementation.
        Actual API integration will be added later.
        """

        return {
            "success": False,
            "provider": self.name,
            "image_url": None,
            "error": "Hugging Face provider is not configured yet."
        }
