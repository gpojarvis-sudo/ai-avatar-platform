from io import BytesIO
from typing import Any, Dict

from huggingface_hub import AsyncInferenceClient
from huggingface_hub.utils import HfHubHTTPError
from PIL import Image
from loguru import logger

from config.settings import settings
from .base import BaseImageProvider


class HuggingFaceProvider(BaseImageProvider):

    name = "huggingface"

    def __init__(self):
        self.client = AsyncInferenceClient(
            provider=settings.HUGGINGFACE_PROVIDER,
            api_key=settings.HUGGINGFACE_API_KEY,
            timeout=settings.HUGGINGFACE_TIMEOUT,
        )

        self.model = settings.HUGGINGFACE_MODEL

    async def generate(
        self,
        prompt: str,
        **kwargs,
    ) -> Dict[str, Any]:

        try:

            logger.info(
                f"Provider : {settings.HUGGINGFACE_PROVIDER}"
            )

            logger.info(
                f"Model : {self.model}"
            )

            image: Image.Image = await self.client.text_to_image(
                prompt=prompt,
                model=self.model,
                num_inference_steps=4,
            )

            buffer = BytesIO()

            image.save(
                buffer,
                format="PNG",
            )

            return {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "image_bytes": buffer.getvalue(),
            }

        except HfHubHTTPError as e:

            logger.exception("Hugging Face HTTP Error")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": str(e),
            }

        except Exception as e:

            logger.exception("Unexpected Hugging Face Error")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": str(e),
            }
