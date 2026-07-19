from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ======================================================
    # Application
    # ======================================================

    APP_NAME: str = "AI Avatar Platform"
    APP_VERSION: str = "1.0.0"

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
    # AI Providers
    # ======================================================

    HUGGINGFACE_API_KEY: str = ""

    NVIDIA_API_KEY: str = ""

    GEMINI_API_KEY: str = ""

    GROQ_API_KEY: str = ""

    # ======================================================
    # Default Providers
    # ======================================================

    DEFAULT_IMAGE_PROVIDER: str = "huggingface"

    DEFAULT_LLM_PROVIDER: str = "groq"

    REQUEST_TIMEOUT: int = 60

    # ======================================================
    # Hugging Face
    # ======================================================

    HUGGINGFACE_MODEL: str = (
        "black-forest-labs/FLUX.1-schnell"
    )

    HUGGINGFACE_BASE_URL: str = (
        "https://router.huggingface.co/hf-inference/models"
    )

    HUGGINGFACE_TIMEOUT: int = 120

    # ======================================================
    # Environment
    # ======================================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
