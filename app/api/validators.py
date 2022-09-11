from collections import defaultdict
from datetime import datetime
from dateutil import tz, parser
from http import HTTPStatus
from typing import Any, List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import BaseCRUD, ModelType


async def try_get_object_by_attribute(
        crud_obj: BaseCRUD,
        attr_name: str,
        attr_value: Any,
        session: AsyncSession
) -> ModelType:
    result = await crud_obj.get_by_attributes(
        {attr_name: attr_value}, session
    )
    if result is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=(
                f'{crud_obj.model.__name__} '
                f'with {attr_name}={attr_value} not found!'
            )
        )
    return result


def parse_and_check_date(date: str) -> datetime:
    try:
        date = parser.isoparse(date)
    except ValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Invalid date format'
        )
    if date > datetime.now(tz.tzutc()):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                f'date in UTC cant be larger then '
                f'{datetime.now(tz.tzutc())}'
            )
        )
    return date
