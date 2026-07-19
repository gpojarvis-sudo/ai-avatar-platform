from pathlib import Path

from shared.logger import logger
from shared.utils import ensure_directory, generate_filename


class AvatarService:
    """
    Basic Avatar Animation Service (MVP)

    This service prepares avatar animation jobs.
    Real integration with SadTalker, LivePortrait,
    OmniAvatar, etc. will be added later.
    """

    def __init__(self):
        self.output_dir = ensure_directory("static/avatars")

    async def generate(
        self,
        image_path: str,
        audio_path: str,
        provider: str = "sadtalker",
        extension: str = "mp4",
    ):

        filename = generate_filename(
            extension=extension,
            prefix="avatar",
        )

        output_path = Path(self.output_dir) / filename

        logger.info(
            f"Avatar generation requested using '{provider}'"
        )

        logger.info(f"Image : {image_path}")
        logger.info(f"Audio : {audio_path}")

        return {
            "success": True,
            "provider": provider,
            "image_path": image_path,
            "audio_path": audio_path,
            "filename": filename,
            "output_path": str(output_path),
            "message": (
                "Avatar provider integration "
                "will be added in the next step."
            ),
        }


avatar_service = AvatarService()
