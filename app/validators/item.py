from collections import defaultdict
from http import HTTPStatus
from typing import Any, List

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import BaseCRUD, ModelType
from app.crud.system_item import system_item_crud
from app.schemas.system_item import SystemItemCreate
from app.models import SystemItem, SystemItemType


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


def check_type_unchanged(
        item: SystemItemCreate, item_obj: SystemItem
) -> None:
    if item.type != item_obj.type:
        raise RequestValidationError('You cannot change type of Item')


async def check_parent_id_in_package(
        items: List[SystemItemCreate], session: AsyncSession
) -> None:
    parents_approved = set()
    for item in sorted(items, key=lambda x: x.type, reverse=True):
        if (
                item.parent_id is not None and
                item.parent_id not in parents_approved
        ):
            parent = await system_item_crud.get(
                pk=item.parent_id, session=session
            )
            if parent is None or parent.type == SystemItemType.FILE:
                raise RequestValidationError(
                    f'Parent with id {item.parent_id} dont exist'
                )
            elif parent.type == SystemItemType.FILE:
                raise RequestValidationError(
                    f'Item with type {SystemItemType.FILE.value} '
                    f'cant be parent'
                )
            parents_approved.add(item.parent_id)
        if item.type == SystemItemType.FOLDER:
            parents_approved.add(item.id)
