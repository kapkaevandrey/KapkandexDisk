from collections import deque
from datetime import datetime
from typing import List, Set, Collection

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.system_item import SystemItemListCreate
from app.models import SystemItem


async def update_or_create_items_form_package(
        session: AsyncSession,
        items_data: SystemItemListCreate
):
    date = items_data.date


async def update_parents_size(
        parents_ids: Collection,
        date: datetime,
        session: AsyncSession,
        commit=False
) -> List[SystemItem]:
    """Update SystemType objects with type folder"""
    updated_folders = []
    # code update parent need construct graph
    if commit:
        session.add_all(tuple(updated_folders))
        await session.commit()
        [await session.refresh(folder) for folder in updated_folders]
    return updated_folders



