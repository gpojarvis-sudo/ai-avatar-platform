from pathlib import Path

from shared.logger import logger
from shared.utils import ensure_directory, generate_filename
from shared.constants import SUPPORTED_IMAGE_FORMATS
from image_service.providers.manager import ImageProviderManager


class ImageService:
    """
    Basic Image Service (MVP)
    """

    def __init__(self):
        self.output_dir = ensure_directory("static/images")
        self.provider_manager = ImageProviderManager()

    async def generate(
        self,
        prompt: str,
        provider: str = "gemini",
        extension: str = "png",
    ):
        if extension.lower() not in SUPPORTED_IMAGE_FORMATS:
            raise ValueError(
                f"Unsupported image format: {extension}"
            )

        filename = generate_filename(
            extension=extension,
            prefix="image",
        )

        output_path = Path(self.output_dir) / filename

        logger.info(
            f"Image generation requested using '{provider}'"
        )

        logger.info(f"Prompt: {prompt}")

        provider_result = await self.provider_manager.generate(
            prompt=prompt
        )

        logger.info(
            f"Provider Manager Result: {provider_result}"
        )

        return {
            "success": True,
            "provider": provider,
            "prompt": prompt,
            "filename": filename,
            "output_path": str(output_path),
            "provider_result": provider_result,
        }


image_service = ImageService()
