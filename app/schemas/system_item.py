from datetime import datetime
import re
from typing import Optional, List

from pydantic import (
    BaseModel, PositiveInt, Field, validator, root_validator
)

from app.models import SystemItemType
from app.core.config import settings

class SystemItemBase(BaseModel):
    id: str = Field()
    url: Optional[str] = Field(max_length=255)
    parent_id: Optional[str] = Field(alias='parentId')
    type: SystemItemType
    size: Optional[PositiveInt]

    @validator('update_date', pre=True)
    def validate_date_format(cls, value):
        if not re.match(
                settings.date_matching_pattern, value
        ):
            raise ValueError('Invalid date format')
        return value

    class Config:
        allow_population_by_field_name = True
        min_anystr_length = 1


class SystemItemCreate(SystemItemBase):
    pass


class SystemItemListCreate(BaseModel):
    items: List[SystemItemCreate]
    update_date: datetime = Field(
        alias='updateDate', regex=settings.date_matching_pattern
    )

    @validator('update_date')
    def validate_date_format(cls, value):
        return value

