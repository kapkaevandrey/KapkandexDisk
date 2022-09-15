from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'KapkandexDisk'
    app_description: str = 'Service for remote file storage'
    database_url: str = 'sqlite+aiosqlite:///./test.db'
    secret: str = 'where is my money lebowski'

    class Config:
        env_file = '.env'


settings = Settings()
