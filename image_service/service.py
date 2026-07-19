from pathlib import Path

from config.settings import settings

from image_service.providers.manager import ImageProviderManager
from shared.utils import ensure_directory, generate_filename


class ImageService:

    def __init__(self):

        self.provider_manager = ImageProviderManager()

        ensure_directory("static/images")

    async def generate(
        self,
        prompt: str,
        negative_prompt: str = "",
        aspect_ratio: str = "1:1",
        quality: str = "balanced",
        seed: int | None = None,
        provider: str | None = None,
        model: str | None = None,
        extension: str = "png",
    ):

        extension = extension.lower()

        if extension not in [
            "png",
            "jpg",
            "jpeg",
            "webp",
        ]:
            raise ValueError(
                "Unsupported image extension."
            )

        supported_aspect_ratios = [
            "1:1",
            "9:16",
            "16:9",
            "4:5",
            "3:2",
        ]

        if aspect_ratio not in supported_aspect_ratios:
            aspect_ratio = "1:1"

        if provider is None:
            provider = settings.DEFAULT_IMAGE_PROVIDER

        if model is None:

            if provider == "cloudflare":
                model = settings.CLOUDFLARE_IMAGE_MODEL

            elif provider == "huggingface":
                model = "flux-dev"

            else:
                model = ""

        aspect_ratio_sizes = {
            "1:1": (1024, 1024),
            "9:16": (768, 1365),
            "16:9": (1365, 768),
            "4:5": (1024, 1280),
            "3:2": (1152, 768),
        }

        width, height = aspect_ratio_sizes[aspect_ratio]

        quality_steps = {
            "fast": 4,
            "balanced": 12,
            "ultra": 28,
        }

        steps = quality_steps.get(
            quality,
            12,
        )

        result = await self.provider_manager.generate(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            steps=steps,
            seed=seed,
            provider=provider,
            model=model,
        )

        if not result["success"]:
            return result

        filename = generate_filename(extension)

        output_path = Path(
            "static/images"
        ) / filename

        output_path.write_bytes(
            result["image_bytes"]
        )

        image_url = (
            f"{settings.PUBLIC_BASE_URL}"
            f"/static/images/{filename}"
        )

        return {
            "success": True,
            "provider": result["provider"],
            "model": result["model"],
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "aspect_ratio": aspect_ratio,
            "quality": quality,
            "seed": seed,
            "filename": filename,
            "image_url": image_url,
        }
