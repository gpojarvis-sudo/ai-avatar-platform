from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from image_service.routes import router as image_router
from tts_service.routes import router as tts_router
from avatar_service.routes import router as avatar_router
from video_service.routes import router as video_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Avatar Platform",
        description="Modular AI Avatar Platform MVP",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    @app.get("/")
    async def root():
        return {
            "success": True,
            "message": "AI Avatar Platform API is running."
        }

    @app.get("/health")
    async def health():
        return {
            "status": "healthy",
            "version": "1.0.0"
        }

    # --------------------------------------------------
    # Create Static Directories
    # --------------------------------------------------
    Path("static/images").mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------
    # Serve Static Files
    # --------------------------------------------------
    app.mount(
        "/static",
        StaticFiles(directory="static"),
        name="static",
    )

    # --------------------------------------------------
    # Register API Routes
    # --------------------------------------------------
    app.include_router(image_router, prefix="/api/v1")
    app.include_router(tts_router, prefix="/api/v1")
    app.include_router(avatar_router, prefix="/api/v1")
    app.include_router(video_router, prefix="/api/v1")

    return app


app = create_app()
