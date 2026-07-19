from tts_service.providers.manager import provider_manager
from tts_service.schemas import (
    TTSRequest,
    TTSResponse,
)


class TTSService:
    """
    Business logic layer for TTS generation.
    """

    async def generate(
        self,
        request: TTSRequest,
    ) -> TTSResponse:
        """
        Generate speech using the selected provider.
        """

        provider = provider_manager.get(
            request.provider
        )

        return await provider.generate(request)

    async def get_available_providers(
        self,
    ) -> list[str]:
        """
        Get all registered providers.
        """

        return provider_manager.available()

    async def health(self) -> dict:
        """
        Health status of all providers.
        """

        return await provider_manager.health()


tts_service = TTSService()
