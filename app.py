from fastapi import FastAPI

app = FastAPI(
    title="AI Avatar Platform",
    description="A modular AI platform for image generation, text-to-speech, avatar animation, and video creation.",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "project": "AI Avatar Platform",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
