from fastapi import FastAPI

from config.settings import settings


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI(
        title=settings.APP_NAME,
        description=(
            "A modular AI platform for image generation, "
            "text-to-speech, avatar animation, and video creation."
        ),
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    @app.get("/", tags=["System"])
    async def root():
        return {
            "project": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "status": "running",
        }

    @app.get("/health", tags=["System"])
    async def health():
        return {
            "status": "healthy",
            "version": settings.APP_VERSION,
        }

    return app


app = create_app()
