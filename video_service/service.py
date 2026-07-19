from pathlib import Path

from shared.logger import logger
from shared.utils import ensure_directory, generate_filename


class VideoService:
    """
    Basic Video Composition Service (MVP)

    This service prepares the final video generation job.

    Real integration with FFmpeg,
    MoviePy,
    Remotion,
    or cloud video engines
    will be added later.
    """

    def __init__(self):
        self.output_dir = ensure_directory("static/videos")

    async def generate(
        self,
        image_path: str,
        audio_path: str,
        avatar_path: str = "",
        provider: str = "ffmpeg",
        extension: str = "mp4",
    ):

        filename = generate_filename(
            extension=extension,
            prefix="video",
        )

        output_path = Path(self.output_dir) / filename

        logger.info(
            f"Video generation requested using '{provider}'"
        )

        logger.info(f"Image : {image_path}")
        logger.info(f"Audio : {audio_path}")
        logger.info(f"Avatar : {avatar_path}")

        return {
            "success": True,
            "provider": provider,
            "image_path": image_path,
            "audio_path": audio_path,
            "avatar_path": avatar_path,
            "filename": filename,
            "output_path": str(output_path),
            "message": (
                "Video composition integration "
                "will be added in the next step."
            ),
        }


video_service = VideoService()
