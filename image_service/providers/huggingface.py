import httpx
from typing import Any, Dict

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

        try:

            async with httpx.AsyncClient(
                timeout=self.timeout
            ) as client:

                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                )

            if response.status_code != 200:

                return {
                    "success": False,
                    "provider": self.name,
                    "model": self.model,
                    "error": response.text,
                }

            return {
                "success": True,
                "provider": self.name,
                "model": self.model,
                "image_bytes": response.content,
            }

        except httpx.TimeoutException:

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": "Request timed out."
            }

        except Exception as e:

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": str(e),
            }
