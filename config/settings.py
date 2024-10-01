from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration settings for the FastAPI application.

    The settings are automatically
    loaded from the specified `.env` file, and can be overridden by
    corresponding environment variables.
    """

    app_name: str = "Rapid RAG"
    upload_folder_path: str  # correlates to the same name found in the .env

    class Config:
        env_file = ".env"


settings = Settings()
