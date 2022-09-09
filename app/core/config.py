from datetime import timedelta

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'KapkandexDisk'
    app_description: str = 'Service for remote file storage'
    database_url: str
    secret: str = 'where is my money lebowski'
    statistic_time_period: timedelta = timedelta(hours=24)

    class Config:
        env_file = '.env'


settings = Settings()
