from datetime import timedelta
import re

from pydantic import BaseSettings

import constants

class Settings(BaseSettings):
    app_title: str = 'KapkandexDisk'
    app_description: str = 'Service for remote file storage'
    database_url: str
    secret: str = 'where is my money lebowski'
    statistic_time_period: timedelta = timedelta(hours=24)
    date_matching_pattern = re.compile(
        constants.DATE_ISO_ZULU_FORMAT_TEMPLATE
    )

    class Config:
        env_file = '.env'


settings = Settings()
