from pathlib import Path
from uuid import uuid4
from datetime import datetime
from typing import Optional


def ensure_directory(path: str | Path) -> Path:
    """
    Create a directory if it does not exist.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def generate_filename(
    extension: str,
    prefix: Optional[str] = None,
) -> str:
    """
    Generate a unique filename.

    Example:
    image_20260719_ab12cd34.png
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = uuid4().hex[:8]

    if prefix:
        return f"{prefix}_{timestamp}_{unique_id}.{extension}"

    return f"{timestamp}_{unique_id}.{extension}"


def get_file_extension(filename: str) -> str:
    """
    Return file extension without dot.
    """

    return Path(filename).suffix.replace(".", "").lower()


def is_supported_extension(
    filename: str,
    supported_extensions: tuple | list,
) -> bool:
    """
    Check whether a file extension is supported.
    """

    extension = get_file_extension(filename)
    return extension in supported_extensions
