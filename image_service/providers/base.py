from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseImageProvider(ABC):
    """
    Base class for all image generation providers.
    Every provider must implement generate().
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
            {
                "success": True/False,
                "provider": "...",
                "image_url": "...",
                "error": None
            }
        """
        pass
