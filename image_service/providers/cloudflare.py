import httpx
from loguru import logger

from config.settings import settings
from .base import BaseImageProvider


class CloudflareProvider(BaseImageProvider):
    PROVIDER_NAME = "cloudflare"

    async def generate(self, prompt: str, **kwargs):

        model = kwargs.get(
            "model",
            settings.CLOUDFLARE_IMAGE_MODEL,
        )

        url = (
            f"https://api.cloudflare.com/client/v4/accounts/"
            f"{settings.CLOUDFLARE_ACCOUNT_ID}"
            f"/ai/run/{model}"
        )

        headers = {
            "Authorization": f"Bearer {settings.CLOUDFLARE_API_TOKEN}",
        }

        payload = {
            "prompt": prompt,
        }

        if kwargs.get("seed") is not None:
            payload["seed"] = kwargs["seed"]

        if kwargs.get("steps") is not None:
            payload["num_steps"] = kwargs["steps"]

        if kwargs.get("width"):
            payload["width"] = kwargs["width"]

        if kwargs.get("height"):
            payload["height"] = kwargs["height"]

        logger.info("=" * 60)
        logger.info("Cloudflare Workers AI")
        logger.info(f"URL : {url}")
        logger.info(f"MODEL : {model}")
        logger.info(f"PAYLOAD : {payload}")
        logger.info("=" * 60)

        try:

            async with httpx.AsyncClient(
                timeout=settings.CLOUDFLARE_TIMEOUT
            ) as client:

                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                )

            logger.info(f"Status : {response.status_code}")
            logger.info(f"Content-Type : {response.headers.get('content-type')}")

            response.raise_for_status()

            content_type = response.headers.get(
                "content-type",
                "",
            )

            # Image returned directly
            if content_type.startswith("image/"):

                return {
                    "success": True,
                    "provider": self.PROVIDER_NAME,
                    "model": model,
                    "image_bytes": response.content,
                }

            # JSON response
            data = response.json()

            logger.info(data)

            if (
                data.get("success") is False
                or data.get("errors")
            ):
                return {
                    "success": False,
                    "provider": self.PROVIDER_NAME,
                    "model": model,
                    "error": str(data),
                }

            result = data.get("result")

            if isinstance(result, str):

                return {
                    "success": True,
                    "provider": self.PROVIDER_NAME,
                    "model": model,
                    "image_bytes": result.encode(),
                }

            return {
                "success": False,
                "provider": self.PROVIDER_NAME,
                "model": model,
                "error": f"Unexpected response: {data}",
            }

        except Exception as e:

            logger.exception(e)

            return {
                "success": False,
                "provider": self.PROVIDER_NAME,
                "model": model,
                "error": str(e),
            }
