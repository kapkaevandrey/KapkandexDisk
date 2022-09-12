from __future__ import annotations
from datetime import datetime
import re
from typing import Optional, List

from pydantic import (
    BaseModel, PositiveInt, Field, validator, root_validator
)

from app.models import SystemItemType
from app.core.constants import DATE_ISO_ZULU_FORMAT_TEMPLATE
from app.utils.convertors import convert_datetime_to_utc


class SystemItemBase(BaseModel):
    id: str = Field()
    url: Optional[str] = Field(max_length=255)
    parent_id: Optional[str] = Field(alias='parentId')
    type: SystemItemType
    size: Optional[PositiveInt]

    class Config:
        allow_population_by_field_name = True
        min_anystr_length = 1


class SystemItemCreate(SystemItemBase):
    @root_validator(skip_on_failure=True)
    def check_fields_is_none_when_type_folder(cls, values):
        is_folder = values['type'] == SystemItemType.FOLDER.value
        is_file = values['type'] == SystemItemType.FILE.value
        for field_name in ['url', 'size']:
            if is_folder and values[field_name] is not None:
                raise ValueError(
                    f'field {field_name} most be None for file type - '
                    f'{SystemItemType.FOLDER.value}')
            if is_file and values[field_name] is None:
                raise ValueError(
                    f'field {field_name} cant be None for file type - '
                    f'{SystemItemType.FILE.value}')
        return values

    @root_validator(skip_on_failure=True)
    def check_id_not_equal_aprent_id(cls, values):
        if values['id'] == values['parent_id']:
            raise ValueError(
                'Filed id cant be equal parent_id'
            )
        return values


class SystemItemRead(SystemItemBase):
    date: datetime

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: convert_datetime_to_utc
        }


class SystemItemUpdate(SystemItemCreate):
    ...


class SystemItemFullRead(SystemItemRead):
    children: Optional[List[SystemItemFullRead]]


class SystemItemListCreate(BaseModel):
    items: List[SystemItemCreate]
    date: datetime = Field(alias='updateDate')

    @validator('date', pre=True)
    def validate_date_format(cls, value):
        if not re.match(
                DATE_ISO_ZULU_FORMAT_TEMPLATE, value
        ):
            raise ValueError('Invalid date format')
        return value

    class Config:
        allow_population_by_field_name = True
