from typing import Dict

from config.settings import settings

from tts_service.providers.base import BaseTTSProvider


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
            raise ValueError(
                f"TTS provider '{provider}' is not registered."
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
            except Exception:
                result[name] = False

        return result


provider_manager = TTSProviderManager()
