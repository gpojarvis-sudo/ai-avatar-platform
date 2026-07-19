from typing import Dict

from config.settings import settings

from tts_service.providers.base import BaseTTSProvider

from tts_service.providers.elevenlabs import ElevenLabsProvider
# Future Providers
# from tts_service.providers.edge_tts import EdgeTTSProvider
# from tts_service.providers.kokoro import KokoroProvider
# from tts_service.providers.gemini import GeminiProvider


class TTSProviderManager:
    """
    Central manager responsible for:

    - Registering providers
    - Selecting providers
    - Returning the active provider
    - Future fallback support
    """

    def __init__(self):
        self._providers: Dict[str, BaseTTSProvider] = {}

        # Register Providers
        self._register_providers()

    def _register_providers(self) -> None:
        """
        Register all available providers.
        """

        self.register(ElevenLabsProvider())

        # Register future providers here
        # self.register(EdgeTTSProvider())
        # self.register(KokoroProvider())
        # self.register(GeminiProvider())

    def register(self, provider: BaseTTSProvider) -> None:
        """
        Register a provider instance.
        """
        self._providers[provider.name.lower()] = provider

    def get(self, provider_name: str | None = None) -> BaseTTSProvider:
        """
        Get a provider by name.
        Falls back to DEFAULT_TTS_PROVIDER.
        """

        provider = (
            provider_name
            or settings.DEFAULT_TTS_PROVIDER
        ).lower()

        if provider not in self._providers:
            available = ", ".join(self.available())

            raise ValueError(
                f"TTS provider '{provider}' is not registered. "
                f"Available providers: {available}"
            )

        return self._providers[provider]

    def available(self) -> list[str]:
        """
        List all registered providers.
        """
        return sorted(self._providers.keys())

    async def health(self) -> dict:
        """
        Check health of all registered providers.
        """

        result = {}

        for name, provider in self._providers.items():
            try:
                result[name] = await provider.health_check()
            except Exception as e:
                result[name] = {
                    "healthy": False,
                    "error": str(e)
                }

        return result


# Singleton Instance
provider_manager = TTSProviderManager()
