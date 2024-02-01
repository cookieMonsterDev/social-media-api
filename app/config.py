from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file='.env')

@lru_cache
def get_settings () -> Settings:
  return Settings()
