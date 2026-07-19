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

        provider_order = []

        if provider in self.providers:
            provider_order.append(provider)

        for provider_name in self.providers:

            if provider_name not in provider_order:
                provider_order.append(provider_name)

        last_error = "Unknown error"

        for provider_name in provider_order:

            provider_instance = self.providers[provider_name]

            result = await provider_instance.generate(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                steps=steps,
                seed=seed,
                model=model,
            )

            if result.get("success"):

                return result

            last_error = result.get(
                "error",
                "Unknown provider error",
            )

        return {
            "success": False,
            "provider": provider,
            "model": model,
            "error": last_error,
        }
