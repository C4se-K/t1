


from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env", extra = "ignore")

    APP_NAME:str = "Event Ingestion API"
    LOG_LEVEL:str = "INFO"

    ALLOWED_ORIGINS: List[str] = ["*"]

settings = Settings()

