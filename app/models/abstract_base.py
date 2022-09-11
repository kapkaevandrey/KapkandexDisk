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

    @property
    def is_file(self) -> bool:
        return self.type == SystemItemType.FILE

    @property
    def is_folder(self) -> bool:
        return self.type == SystemItemType.FOLDER
