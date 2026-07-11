from pydantic_settings import BaseSettings, SettingsConfigDict


# Class settings
class Settings(BaseSettings):
    # PostgreSQL URL
    postgres_url: str = ""

    model_config = SettingsConfigDict(env_file=".env")


# Run the class
settings = Settings()
