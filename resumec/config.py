import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    llm_model: str = "gpt-4o-mini"
    max_retries: int = 3


settings = Settings()
