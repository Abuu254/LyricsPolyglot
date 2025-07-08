from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "LyricsPolyglot"
    DATABASE_URL: str
    REDIS_URL: str
    JWT_SECRET: str
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = None

    class Config:
        env_file = "env.dev"

settings = Settings()