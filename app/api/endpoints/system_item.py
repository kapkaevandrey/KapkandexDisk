from dateutil import parser
from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    try_get_object_by_attribute, parse_and_check_date
)
from app.core.db import get_async_session
from app.core.constants import DATE_ISO_ZULU_FORMAT_REGEX
from app.crud import system_item_crud
from app.schemas.system_item import SystemItemListCreate
from app.utils.update_create_objects import update_parents_size

router = APIRouter()


@router.post(
    '/imports',
    status_code=HTTPStatus.OK
)
async def import_folders_and_files(
        items_data: SystemItemListCreate,
        session: AsyncSession = Depends(get_async_session)
):

    return {'Hello': 'FastAPI'}


@router.delete(
    '/delete/{id}',
    status_code=HTTPStatus.OK,
)
async def delete_folder_or_file(
        id: str,
        date: str = Query(
            regex=DATE_ISO_ZULU_FORMAT_REGEX,
            title='Date in ISO format',
            description='Date in ISO format',
            example='2020-12-31T21:00:00.223Z'
        ),
        session: AsyncSession = Depends(get_async_session)
):
    date = parse_and_check_date(date)
    item = await try_get_object_by_attribute(
        system_item_crud,
        attr_name='id', attr_value=id,
        session=session
    )
    removed_item = await system_item_crud.remove(item, session)
    if item.parent_id is not None:
        await update_parents_size(
            parents_ids=[item.parent_id],
            date=date,
            session=session,
            commit=True
        )

@router.get(
    '/nodes/{id}',
    status_code=HTTPStatus.OK,
)
async def get_item(
        id: str,
        session: AsyncSession = Depends(get_async_session)
):
    await try_get_object_by_attribute(
        system_item_crud, attr_name='id', attr_value=id, session=session
    )
    return id