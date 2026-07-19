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

            logger.info(f"Provider : {settings.HUGGINGFACE_PROVIDER}")
            logger.info(f"Model : {self.model}")

            # --------------------------------------------------
            # Dynamic Steps
            # --------------------------------------------------

            steps = kwargs.get("steps", 30)

            # --------------------------------------------------
            # Prompt Enhancement
            # --------------------------------------------------

            enhanced_prompt = f"""
{prompt}

ultra realistic,
masterpiece,
best quality,
8k UHD,
extremely detailed,
sharp focus,
professional photography,
highly detailed face,
highly detailed eyes,
natural skin texture,
HDR,
cinematic lighting,
award winning photography
""".strip()

            image: Image.Image = await self.client.text_to_image(
                prompt=enhanced_prompt,
                model=self.model,
                num_inference_steps=steps,
            )

            buffer = BytesIO()

            image.save(
                buffer,
                format="PNG",
            )

            logger.success("Image generated successfully")

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
