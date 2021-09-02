from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    client_id : str
    client_secret : str
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()