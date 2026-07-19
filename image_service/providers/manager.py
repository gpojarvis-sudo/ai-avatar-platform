from .huggingface import HuggingFaceProvider
from .nvidia import NvidiaProvider
from .gemini import GeminiProvider


class ImageProviderManager:
    """
    Production Image Provider Manager
    """

    def __init__(self):

        self.providers = {
            "huggingface": HuggingFaceProvider(),
            "nvidia": NvidiaProvider(),
            "gemini": GeminiProvider(),
        }

        self.fallback_order = [
            "huggingface",
            "nvidia",
            "gemini",
        ]

    async def generate(
        self,
        prompt: str,
        provider: str = "huggingface",
        **kwargs,
    ):

        # Try requested provider first
        if provider in self.providers:

            result = await self.providers[
                provider
            ].generate(
                prompt=prompt,
                **kwargs,
            )

            if result.get("success"):
                return result

        # Automatic fallback
        for provider_name in self.fallback_order:

            if provider_name == provider:
                continue

            result = await self.providers[
                provider_name
            ].generate(
                prompt=prompt,
                **kwargs,
            )

            if result.get("success"):
                return result

        return {
            "success": False,
            "provider": provider,
            "model": None,
            "error": "All image providers failed."
        }
