from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from shared.constants import JobStatus, Provider, ServiceType


class BaseJob(BaseModel):
    """
    Base model for all AI processing jobs.
    """

    job_id: str = Field(default_factory=lambda: str(uuid4()))
    service: ServiceType
    provider: Provider

    status: JobStatus = JobStatus.PENDING

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    error_message: Optional[str] = None

    def mark_processing(self):
        self.status = JobStatus.PROCESSING
        self.updated_at = datetime.utcnow()

    def mark_completed(self):
        self.status = JobStatus.COMPLETED
        self.updated_at = datetime.utcnow()

    def mark_failed(self, message: str):
        self.status = JobStatus.FAILED
        self.error_message = message
        self.updated_at = datetime.utcnow()


class ImageJob(BaseJob):
    prompt: str
    output_path: Optional[str] = None


class TTSJob(BaseJob):
    text: str
    voice: str = "default"
    output_path: Optional[str] = None


class AvatarJob(BaseJob):
    image_path: str
    audio_path: str
    output_path: Optional[str] = None


class VideoJob(BaseJob):
    prompt: str
    output_path: Optional[str] = None
