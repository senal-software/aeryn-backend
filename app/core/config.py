from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str

    # Define the location of the .env file
    model_config = SettingsConfigDict()

# Use lru_cache to cache the settings object
@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()