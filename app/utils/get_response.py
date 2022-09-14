from collections import deque

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import system_item_crud
from app.models import SystemItem, SystemItemType
from app.schemas.system_item import SystemItemRead, SystemItemFullRead


async def create_nested_response(
        session: AsyncSession,
        item: SystemItem,
) -> SystemItemFullRead:
    """
    coroutine that creates a response with nested
    objects using a sequential chain of queries to the database
    :param session: AsyncSession by SQLAlchemy
    :param item: SystemItem object from db
    :return: SystemItemFullRead pydantic schemas object
    """
    children_default = {
        SystemItemType.FOLDER: [],
        SystemItemType.FILE: None
    }
    item = SystemItemRead.from_orm(item)
    response = SystemItemFullRead(
        **item.dict(), children=children_default[item.type]
    )
    children_response = deque()
    children_response.append(response)
    while children_response:
        current_item = children_response.popleft()
        children = await system_item_crud.get_by_attributes(
            {'parent_id': current_item.id}, session=session, many=True,
            order_by='date', desc=True
        )
        if children:
            for child in children:
                child_item = SystemItemFullRead(
                    **SystemItemRead.from_orm(child).dict(),
                    children=children_default[child.type.value]
                )
                current_item.children.append(child_item)
                if not child.is_file:
                    children_response.append(child_item)
    return response
