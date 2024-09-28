import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Rapid RAG"
    upload_folder_path: str # correlates to the same name found in the .env

    class Config:
        env_file = '.env'

settings = Settings() 
