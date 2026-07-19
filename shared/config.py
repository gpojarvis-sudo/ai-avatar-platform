from pathlib import Path

from config.settings import settings
from shared.constants import (
    APP_NAME,
    APP_VERSION,
    API_PREFIX,
)

# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = APP_NAME
PROJECT_VERSION = APP_VERSION
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# API
# ==========================================================

API_V1_PREFIX = API_PREFIX

# ==========================================================
# Directories
# ==========================================================

STATIC_DIR = PROJECT_ROOT / "static"

IMAGE_DIR = STATIC_DIR / "images"
AUDIO_DIR = STATIC_DIR / "audio"
VIDEO_DIR = STATIC_DIR / "video"
TEMP_DIR = STATIC_DIR / "temp"

LOG_DIR = PROJECT_ROOT / "logs"

# ==========================================================
# Runtime Configuration
# ==========================================================

DEBUG = settings.DEBUG

HOST = settings.HOST
PORT = settings.PORT

# ==========================================================
# Create Required Directories
# ==========================================================

REQUIRED_DIRECTORIES = [
    IMAGE_DIR,
    AUDIO_DIR,
    VIDEO_DIR,
    TEMP_DIR,
    LOG_DIR,
]

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)
