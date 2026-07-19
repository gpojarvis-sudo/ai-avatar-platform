from image_service.providers.huggingface import HuggingFaceProvider
from image_service.providers.gemini import GeminiProvider
from image_service.providers.nvidia import NvidiaProvider


class ImageProviderManager:

    def __init__(self):

        self.providers = {
            "huggingface": HuggingFaceProvider(),
            "gemini": GeminiProvider(),
            "nvidia": NvidiaProvider(),
        }

    async def generate(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: int = 1024,
        height: int = 1024,
        steps: int = 12,
        seed: int | None = None,
        provider: str = "huggingface",
        model: str = "flux-dev",
    ):

        # -------------------------------
        # Validate Provider
        # -------------------------------

        if provider not in self.providers:

            return {
                "success": False,
                "provider": provider,
                "model": model,
                "error": f"Unknown provider: {provider}",
            }

        # -------------------------------
        # Call Only Requested Provider
        # -------------------------------

        provider_instance = self.providers[provider]

        result = await provider_instance.generate(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            steps=steps,
            seed=seed,
            model=model,
        )

        return result
