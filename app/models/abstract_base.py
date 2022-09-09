import enum

from sqlalchemy import (
    Column, DateTime, String, Enum, Integer
)
from sqlalchemy.orm import validates

from app.core.db import Base


class SystemItemType(str, enum.Enum):
    FILE = 'FILE'
    FOLDER = 'FOLDER'


class SystemItemBase(Base):
    __abstract__ = True

    url = Column(String(255))
    type = Column(Enum(SystemItemType), nullable=False)
    size = Column(Integer)
    date = Column(DateTime(timezone=True))

    @validates('url')
    def validate_url(self, key, url):
        if self.type == SystemItemType.FILE.value and url is not None:
            raise ValueError(
                f'the url field must be None with a value of the Folder type '
                f'{self.type}')
        return url

    @validates('size')
    def validate_url(self, key, size):
        if self.type == SystemItemType.FILE.value and size is not None:
            raise ValueError(
                f'the url field must be None with a value of the Folder type '
                f'{self.type}')
        return size
