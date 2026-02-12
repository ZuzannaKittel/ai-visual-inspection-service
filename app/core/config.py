from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Visual Inspection Service"
    version: str = "0.1.0"
    debug: bool = True

    database_url: str = "postgresql://zuzanna@localhost:5432/ai_service"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
