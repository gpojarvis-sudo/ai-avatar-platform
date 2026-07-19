from abc import ABC, abstractmethod

from tts_service.schemas import TTSRequest, TTSResponse


class BaseTTSProvider(ABC):
    """
    Abstract base class for all TTS providers.

    Every provider must implement this interface so that
    the rest of the application remains provider-independent.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the provider name.
        """
        pass

    @abstractmethod
    async def generate(
        self,
        request: TTSRequest,
    ) -> TTSResponse:
        """
        Generate speech from text.

        Args:
            request: Standard TTS request.

        Returns:
            Standard TTS response.
        """
        pass

    async def health_check(self) -> bool:
        """
        Optional provider health check.

        Override this method if the provider supports
        connectivity or status verification.
        """
        return True
