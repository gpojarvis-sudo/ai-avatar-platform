from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ======================================================
    # Application
    # ======================================================

    APP_NAME: str = "AI Avatar Platform"
    APP_VERSION: str = "2.1.0"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # ======================================================
    # Public URL
    # ======================================================

    PUBLIC_BASE_URL: str = (
        "https://ai-avatar-platform-production.up.railway.app"
    )

    # ======================================================
    # Cloudflare Workers AI
    # ======================================================

    CLOUDFLARE_ACCOUNT_ID: str = ""

    CLOUDFLARE_API_TOKEN: str = ""

    CLOUDFLARE_IMAGE_MODEL=pruna/p-image

    CLOUDFLARE_TIMEOUT: int = 180

    # ======================================================
    # Hugging Face (Fallback)
    # ======================================================

    HUGGINGFACE_API_KEY: str = ""

    HUGGINGFACE_PROVIDER: str = "auto"

    HUGGINGFACE_MODEL: str = (
        "black-forest-labs/FLUX.1-dev"
    )

    HUGGINGFACE_TIMEOUT: int = 120

    # ======================================================
    # Other Providers
    # ======================================================

    GEMINI_API_KEY: str = ""

    NVIDIA_API_KEY: str = ""

    GROQ_API_KEY: str = ""

    # ======================================================
    # Defaults
    # ======================================================

    DEFAULT_IMAGE_PROVIDER: str = "cloudflare"

    DEFAULT_LLM_PROVIDER: str = "groq"

    REQUEST_TIMEOUT: int = 60

    # ======================================================
    # Environment
    # ======================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
print("ACCOUNT:", settings.CLOUDFLARE_ACCOUNT_ID)
print("TOKEN LENGTH:", len(settings.CLOUDFLARE_API_TOKEN))
print("MODEL:", settings.CLOUDFLARE_IMAGE_MODEL)
print("DEFAULT:", settings.DEFAULT_IMAGE_PROVIDER)
