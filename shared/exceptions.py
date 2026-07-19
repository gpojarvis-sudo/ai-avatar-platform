from fastapi import HTTPException


class AIAvatarPlatformError(Exception):
    """Base exception for the AI Avatar Platform."""

    def __init__(self, message: str = "An unexpected error occurred."):
        self.message = message
        super().__init__(self.message)


class ProviderError(AIAvatarPlatformError):
    """Raised when an AI provider fails."""


class ConfigurationError(AIAvatarPlatformError):
    """Raised when configuration is invalid."""


class ValidationError(AIAvatarPlatformError):
    """Raised when input validation fails."""


class ResourceNotFoundError(AIAvatarPlatformError):
    """Raised when a requested resource does not exist."""


def http_error(status_code: int, message: str) -> HTTPException:
    """Create a standardized FastAPI HTTP exception."""
    return HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "message": message,
        },
    )
