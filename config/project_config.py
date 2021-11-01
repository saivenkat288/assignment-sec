import logging
import sys
from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from service.logging import InterceptHandler

API_PREFIX = "/api/v1"

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "1.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_URL: str = config("DB_CONNECTION", cast=str,default="")
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=1)

SECRET_KEY: Secret = config("API_KEY", cast=Secret, default="secret")

PROJECT_NAME: str = config("PROJECT_NAME", default="Assignment")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="",
)
