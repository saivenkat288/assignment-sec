from pydantic import BaseSettings
from dotenv import load_dotenv
import os
from functools import lru_cache
load_dotenv(verbose=True)

class Settings(BaseSettings):
    db_password: str = "rootbi2i"
    db_username: str = "postgres"
    class Config:
        env_prefix = "" 
        env_file = "../.env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()