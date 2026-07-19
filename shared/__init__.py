"""
AI Avatar Platform - Shared Package

This package contains common modules shared across all services,
including configuration, constants, schemas, models, logging,
exceptions, and utility functions.
"""

from .config import *
from .constants import *
from .exceptions import *
from .logger import logger
from .models import *
from .schemas import *
from .utils import *

__all__ = [
    "logger",
]
