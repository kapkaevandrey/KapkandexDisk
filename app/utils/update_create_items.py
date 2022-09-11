from datetime import datetime
from typing import List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import system_item_crud
from app.schemas.system_item import SystemItemListCreate
from app.models import SystemItem
from app.api.validators import try_get_object_by_attribute

async def update_or_create_items_form_package(
        session: AsyncSession,
        items_data: SystemItemListCreate
):
    date = items_data.date


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
    counter = 0
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
        current_parent.size = int(amount_size) if amount_size is not None else amount_size
        current_parent.date = date
        updated_parents.append(current_parent)
        if current_parent.parent_id is not None:
            current_parent = await try_get_object_by_attribute(
                system_item_crud,
                attr_name='id', attr_value=current_parent.parent_id,
                session=session
            )
        else:
            current_parent = None
    if commit:
        session.add_all(tuple(updated_parents))
        await session.commit()
        [await session.refresh(folder) for folder in updated_parents]
    return updated_parents
