from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["AI Avatar Platform"],
)


@router.get("/")
async def api_root():
    return {
        "success": True,
        "message": "AI Avatar Platform API is running.",
        "version": "0.1.0",
    }


@router.get("/status")
async def api_status():
    return {
        "success": True,
        "status": "healthy",
    }
