import base64
import httpx
from loguru import logger

from config.settings import settings
from .base import BaseImageProvider


class CloudflareProvider(BaseImageProvider):
    PROVIDER_NAME = "cloudflare"

    async def generate(self, prompt: str, **kwargs):

        logger.info("=" * 60)
        logger.info("Cloudflare Provider Started")
        logger.info(f"Account ID: {settings.CLOUDFLARE_ACCOUNT_ID}")
        logger.info(f"Model: {settings.CLOUDFLARE_IMAGE_MODEL}")
        logger.info(f"Token Length: {len(settings.CLOUDFLARE_API_TOKEN)}")
        logger.info(f"Token Empty: {not bool(settings.CLOUDFLARE_API_TOKEN)}")
        logger.info("=" * 60)

        model = settings.CLOUDFLARE_IMAGE_MODEL

        url = (
            f"https://api.cloudflare.com/client/v4/accounts/"
            f"{settings.CLOUDFLARE_ACCOUNT_ID}/ai/run"
        )

        headers = {
            "Authorization": f"Bearer {settings.CLOUDFLARE_API_TOKEN}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "input": {
                "prompt": prompt,
                "aspect_ratio": kwargs.get("aspect_ratio", "1:1"),
            },
        }

        try:
            async with httpx.AsyncClient(timeout=settings.CLOUDFLARE_TIMEOUT) as client:
                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                )

            logger.info(f"HTTP Status: {response.status_code}")
            logger.info("FULL RESPONSE")
logger.info(response.text)

            response.raise_for_status()

            data = response.json()

            if data.get("state") != "Completed":
                return {
                    "success": False,
                    "provider": self.PROVIDER_NAME,
                    "model": model,
                    "error": str(data),
                }

            image = data["result"]["image"]

            if not image.startswith("data:image"):
                raise ValueError("Unexpected image format")

            image_bytes = base64.b64decode(image.split(",", 1)[1])

            return {
                "success": True,
                "provider": self.PROVIDER_NAME,
                "model": model,
                "image_bytes": image_bytes,
            }

        except Exception as e:
            logger.exception(e)

            return {
                "success": False,
                "provider": self.PROVIDER_NAME,
                "model": model,
                "error": str(e),
            }
