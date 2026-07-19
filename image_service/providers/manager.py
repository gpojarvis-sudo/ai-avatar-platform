from .huggingface import HuggingFaceProvider


class ImageProviderManager:
    """
    Manages all available image providers.
    """

    def __init__(self):
        self.providers = [
            HuggingFaceProvider(),
        ]

    async def generate(self, prompt: str, **kwargs):
        """
        Try providers one by one until one succeeds.
        """

        last_result = None

        for provider in self.providers:

            result = await provider.generate(
                prompt=prompt,
                **kwargs
            )

            if result.get("success"):
                return result

            last_result = result

        return last_result
