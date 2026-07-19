from .huggingface import HuggingFaceProvider
from .nvidia import NvidiaProvider
from .gemini import GeminiProvider


class ImageProviderManager:
    """
    Manages all available image providers.
    """

    def __init__(self):
        self.providers = [
            HuggingFaceProvider(),
            NvidiaProvider(),
            GeminiProvider(),
        ]

    async def generate(self, prompt: str, **kwargs):
        """
        Try each provider until one succeeds.
        """

        last_result = {
            "success": False,
            "provider": None,
            "image_url": None,
            "error": "No provider available."
        }

        for provider in self.providers:

            result = await provider.generate(
                prompt=prompt,
                **kwargs
            )

            if result.get("success"):
                return result

            last_result = result

        return last_result
