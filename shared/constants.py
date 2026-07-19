from enum import Enum

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "AI Avatar Platform"
APP_VERSION = "0.1.0"

# ==========================================================
# Service Types
# ==========================================================

class ServiceType(str, Enum):
    IMAGE = "image"
    TTS = "tts"
    AVATAR = "avatar"
    VIDEO = "video"

# ==========================================================
# Supported AI Providers
# ==========================================================

class Provider(str, Enum):
    GEMINI = "gemini"
    NVIDIA = "nvidia"
    OPENAI = "openai"
    GROQ = "groq"
    HUGGINGFACE = "huggingface"
    REPLICATE = "replicate"
    LOCAL = "local"

# ==========================================================
# Job Status
# ==========================================================

class JobStatus(str, Enum):
    PENDING = "pending"
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

# ==========================================================
# Output Formats
# ==========================================================

SUPPORTED_IMAGE_FORMATS = (
    "png",
    "jpg",
    "jpeg",
    "webp",
)

SUPPORTED_AUDIO_FORMATS = (
    "mp3",
    "wav",
    "ogg",
)

SUPPORTED_VIDEO_FORMATS = (
    "mp4",
    "mov",
    "webm",
)

# ==========================================================
# Default Directories
# ==========================================================

IMAGE_OUTPUT_DIR = "static/images"
AUDIO_OUTPUT_DIR = "static/audio"
VIDEO_OUTPUT_DIR = "static/video"
TEMP_OUTPUT_DIR = "static/temp"

# ==========================================================
# API Version
# ==========================================================

API_PREFIX = "/api/v1"

# ==========================================================
# Default Timeouts
# ==========================================================

DEFAULT_HTTP_TIMEOUT = 120
DEFAULT_RETRY_COUNT = 3
