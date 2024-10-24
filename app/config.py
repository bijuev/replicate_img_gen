from pydantic_settings import BaseSettings
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()

class Settings(BaseSettings):
    replicate_api_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8' 

settings = Settings()

