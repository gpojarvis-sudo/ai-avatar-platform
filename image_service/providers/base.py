from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseImageProvider(ABC):
    """
    Base class for all image generation providers.

    Every provider must implement generate() and return
    a standardized response dictionary.
    """

    name = "base"

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate an image from a prompt.

        Returns:

        Success:
        {
            "success": True,
            "provider": "huggingface",
            "model": "black-forest-labs/FLUX.1-schnell",
            "image_bytes": b"..."
        }

        Failure:
        {
            "success": False,
            "provider": "huggingface",
            "model": "black-forest-labs/FLUX.1-schnell",
            "error": "Reason for failure"
        }
        """
        pass
