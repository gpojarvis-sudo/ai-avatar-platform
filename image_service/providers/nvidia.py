from .base import BaseImageProvider


class NvidiaProvider(BaseImageProvider):
    """
    NVIDIA Image Generation Provider
    """

    name = "nvidia"

    async def generate(self, prompt: str, **kwargs):
        """
        Temporary placeholder implementation.
        Actual NVIDIA NIM integration will be added later.
        """

        return {
            "success": False,
            "provider": self.name,
            "image_url": None,
            "error": "NVIDIA provider is not configured yet."
        }
