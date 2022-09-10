from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv('.env')


class Settings(BaseSettings):
    app_title: str = 'KapkandexDisk'
    app_description: str = 'Service for remote file storage'
    database_url: str = 'sqlite+aiosqlite:///./disk.db'
    secret: str = 'where is my money lebowski'

    class Config:
        env_file = '.env'


settings = Settings()
