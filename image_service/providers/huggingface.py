import json
from typing import Any, Dict

import httpx
from loguru import logger

from config.settings import settings
from .base import BaseImageProvider


class HuggingFaceProvider(BaseImageProvider):
    """
    Hugging Face Image Provider
    Production Debug Version
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
        **kwargs,
    ) -> Dict[str, Any]:

        if not self.api_key:
            logger.error("HUGGINGFACE_API_KEY is missing.")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": "HUGGINGFACE_API_KEY is not configured.",
            }

        url = f"{self.base_url}/{self.model}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "image/png",
            "Content-Type": "application/json",
        }

        payload = {
            "inputs": prompt,
            "parameters": {
                "num_inference_steps": 4
            }
        }

        logger.info("=" * 70)
        logger.info("HUGGING FACE REQUEST START")
        logger.info(f"Endpoint : {url}")
        logger.info(f"Model    : {self.model}")
        logger.info(f"Prompt   : {prompt}")

        try:

            async with httpx.AsyncClient(
                timeout=self.timeout
            ) as client:

                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                )

            logger.info("=" * 70)
            logger.info("HUGGING FACE RESPONSE")
            logger.info(f"Status Code : {response.status_code}")
            logger.info(
                f"Content-Type : {response.headers.get('content-type')}"
            )
            logger.info(f"Headers : {dict(response.headers)}")

            body = response.text

            if len(body) > 4000:
                body = body[:4000]

            logger.info(f"Body : {body}")

            if response.status_code != 200:

                try:
                    error_json = response.json()
                    error_message = json.dumps(
                        error_json,
                        indent=2
                    )
                except Exception:
                    error_message = response.text

                logger.error(
                    f"Hugging Face HTTP Error {response.status_code}"
                )

                return {
                    "success": False,
                    "provider": self.name,
                    "model": self.model,
                    "error": (
                        f"HTTP {response.status_code}\n"
                        f"{error_message}"
                    ),
                }

            content_type = (
                response.headers
                .get("content-type", "")
                .lower()
            )

            if "image" not in content_type:

                logger.error(
                    "Expected image but received non-image response."
                )

                return {
                    "success": False,
                    "provider": self.name,
                    "model": self.model,
                    "error": body,
                }

            logger.success(
                f"Image generated successfully "
                f"({len(response.content)} bytes)"
            )

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
                "error": "Request timed out.",
            }

        except httpx.HTTPError as e:

            logger.exception("HTTP Client Error")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": str(e),
            }

        except Exception as e:

            logger.exception("Unexpected Hugging Face Exception")

            return {
                "success": False,
                "provider": self.name,
                "model": self.model,
                "error": str(e),
            }
