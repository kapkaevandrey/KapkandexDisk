from collections import defaultdict
from datetime import datetime
from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import system_item_crud
from app.schemas.system_item import SystemItemListCreate, SystemItemCreate
from app.models import SystemItem
from app.validators.item import (
    try_get_object_by_attribute,
    check_type_unchanged
)


async def create_update_items_process(
        session: AsyncSession,
        items_data: SystemItemListCreate
):
    date = items_data.date
    need_update_ids = set()
    updated_objects = []
    for item in items_data.items:
        item_obj = await system_item_crud.get(pk=item.id, session=session)
        if item_obj is None:
            item_obj = await system_item_crud.create(
                data=item, session=session,
                date=date, commit=False
            )
            if item_obj.parent_id is not None:
                need_update_ids.add(item_obj.parent_id)
        else:
            check_type_unchanged(item, item_obj)
            need_update_ids.update(
                get_parent_item_id_need_update(item, item_obj)
            )
            if (
                    item_obj.is_file
                    and item.parent_id is not None
                    and item.size != item_obj.size
            ):
                need_update_ids.add(item.parent_id)
            item_obj = await system_item_crud.update(
                item_obj, item, session, commit=False, date=date
            )
        updated_objects.append(item_obj)
    session.add_all(updated_objects)
    await session.commit()
    [await session.refresh(item_obj) for item_obj in updated_objects]
    for paren_id in need_update_ids:
        await update_single_parent_size(paren_id, date, session, commit=True)


def get_parent_item_id_need_update(
        item: SystemItemCreate,
        item_obj: SystemItem
) -> set:
    need_update = set()
    if item.parent_id == item_obj.parent_id:
        return need_update
    return set(
        val for val in (item.parent_id, item_obj.parent_id)
        if val is not None
    )


async def update_single_parent_size(
        parent_id: str,
        date: datetime,
        session: AsyncSession,
        commit=False
) -> List[SystemItem]:
    """Update SystemType objects with type folder"""
    current_parent = await try_get_object_by_attribute(
        system_item_crud,
        attr_name='id', attr_value=parent_id,
        session=session
    )
    checked_id = set(current_parent.id)
    updated_parents = []
    while current_parent is not None:
        result = await session.execute(
            select(
                func.sum(SystemItem.size)
            ).where(
                SystemItem.parent_id == current_parent.id,
                SystemItem.size is not None
            )
        )
        amount_size = result.first()[0]
        current_parent.size = (
            int(amount_size) if amount_size is not None else amount_size
        )
        current_parent.date = date
        checked_id.add(current_parent.id)
        updated_parents.append(current_parent)
        if (
                current_parent.parent_id is None
                or current_parent.parent_id in checked_id
        ):
            current_parent = None
        else:
            current_parent = await try_get_object_by_attribute(
                system_item_crud,
                attr_name='id', attr_value=current_parent.parent_id,
                session=session
            )
    if commit:
        session.add_all(tuple(updated_parents))
        await session.commit()
        [await session.refresh(folder) for folder in updated_parents]
    return updated_parents
