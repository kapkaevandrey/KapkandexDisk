from collections import defaultdict
from datetime import datetime
from dateutil import tz, parser
from http import HTTPStatus
from typing import Any, List, Optional

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import BaseCRUD, ModelType
from app.schemas.system_item import SystemItemCreate
from app.models import SystemItem


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
        raise RequestValidationError('Invalid date format')
    check_date_is_valid(date)
    return date


def check_date_is_valid(
        date: datetime, lower_date=Optional[datetime]
) -> None:
    if lower_date is None:
        lower_date = datetime.now(tz.tzutc())
    if date > lower_date:
        raise RequestValidationError(
            f'date in UTC cant be larger then '
            f'{lower_date}'
        )


def check_items_package_unique_id(
        items: List[SystemItemCreate],
) -> None:
    uniq_id_counter = defaultdict(int)
    for item in items:
        uniq_id_counter[item.id] += 1
        if uniq_id_counter[item.id] > 1:
            raise RequestValidationError(
                    f'Items have not unique ids equal id={item.id} '
            )


def check_category_unchanged(item: SystemItemCreate, item_obj: SystemItem):
    if item.type != item_obj.type:
        raise RequestValidationError('You cannot change type of Item')




