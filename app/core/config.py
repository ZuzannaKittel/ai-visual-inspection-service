from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Visual Inspection Service"
    version: str = "0.1.0"
    debug: bool = True

    DATABASE_URL: str
    MODEL_PATH: str = "/app/models/efficientnet_b0.pth"
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
