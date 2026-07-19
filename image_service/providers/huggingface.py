import httpx
from typing import Any, Dict
from loguru import logger

from config.settings import settings
from .base import BaseImageProvider


class HuggingFaceProvider(BaseImageProvider):
    """
    Hugging Face FLUX Image Generation Provider
    """

    name = "huggingface"

    def __init__(self):
        self.api_key = settings.HUGGINGFACE_API_KEY
        self.base_url = settings.HUGGINGFACE_BASE_URL.rstrip("/")
        self.model = settings.HUGGINGFACE_MODEL
        self.timeout = settings.HUGGINGFACE_TIMEOUT

    async def generate(
        self,
        prompt: str,
        **kwargs
    ) -> Dict[str, Any]:

        if not self.api_key:
            logger.error("HUGGINGFACE_API_KEY is missing.")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": "HUGGINGFACE_API_KEY is not configured."
            }

        url = f"{self.base_url}/{self.model}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "image/png",
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "num_inference_steps": 4
            }
        }

        logger.info(f"Using HuggingFace model : {self.model}")
        logger.info(f"Endpoint : {url}")

        try:

            async with httpx.AsyncClient(
                timeout=self.timeout
            ) as client:

                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                )

            logger.info(f"HTTP Status : {response.status_code}")
            logger.info(
                f"Content-Type : {response.headers.get('content-type')}"
            )

            if response.status_code != 200:

                logger.error("Hugging Face returned non-200 response.")
                logger.error(response.text)

                return {
                    "success": False,
                    "provider": self.name,
                    "model": self.model,
                    "error": f"HTTP {response.status_code}: {response.text}",
                }

            content_type = response.headers.get(
                "content-type",
                ""
            ).lower()

            if "image" not in content_type:

                logger.error("Response is not an image.")
                logger.error(response.text)

                return {
                    "success": False,
                    "provider": self.name,
                    "model": self.model,
                    "error": response.text,
                }

            logger.success("Image generated successfully.")

            return {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "image_bytes": response.content,
            }

        except httpx.TimeoutException:

            logger.exception("Hugging Face request timed out.")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": "Request timed out."
            }

        except Exception as e:

            logger.exception("Unexpected Hugging Face error.")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": str(e),
            }
