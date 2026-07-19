from pathlib import Path

from config.settings import settings

from shared.logger import logger
from shared.utils import (
    ensure_directory,
    generate_filename,
)
from shared.constants import SUPPORTED_IMAGE_FORMATS

from image_service.providers.manager import (
    ImageProviderManager,
)


class ImageService:
    """
    Production Image Service
    """

    def __init__(self):

        self.output_dir = ensure_directory(
            "static/images"
        )

        self.provider_manager = (
            ImageProviderManager()
        )

    async def generate(
        self,
        prompt: str,
        provider: str = "huggingface",
        extension: str = "png",
    ):

        extension = extension.lower()

        if extension not in SUPPORTED_IMAGE_FORMATS:

            raise ValueError(
                f"Unsupported image format: {extension}"
            )

        logger.info(
            f"Image generation started using {provider}"
        )

        result = await self.provider_manager.generate(
            prompt=prompt,
            provider=provider,
        )

        if not result.get("success"):
            return result

        filename = generate_filename(
            extension=extension,
            prefix="image",
        )

        output_path = (
            Path(self.output_dir)
            / filename
        )

        with open(
            output_path,
            "wb",
        ) as image_file:

            image_file.write(
                result["image_bytes"]
            )

        image_url = (
            "https://ai-avatar-platform-production.up.railway.app"
            f"/static/images/{filename}"
        )

        logger.success(
            f"Image saved : {output_path}"
        )

        return {

            "success": True,

            "provider": result["provider"],

            "model": result["model"],

            "prompt": prompt,

            "filename": filename,

            "image_url": image_url,

        }


image_service = ImageService()
