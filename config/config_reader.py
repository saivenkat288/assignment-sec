from pydantic import BaseSettings
from dotenv import load_dotenv
import os
from functools import lru_cache
load_dotenv(verbose=True)

class Settings(BaseSettings):
    db_password: str = "cbc456aacc164bb4c3fa7a1c68b0df23c1b42ab818f8ee6fe588bd9d8559b4fd"
    db_username: str = "bdeeqglxayvwpz"
    class Config:
        env_prefix = "" 
        env_file = "../.env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()