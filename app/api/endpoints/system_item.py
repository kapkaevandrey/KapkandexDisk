from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    try_get_object_by_attribute, parse_and_check_date,
    check_items_package_unique_id, check_date_is_valid
)
from app.core.db import get_async_session
from app.core.constants import DATE_ISO_ZULU_FORMAT_REGEX
from app.crud import system_item_crud
from app.schemas.system_item import (
    SystemItemListCreate, SystemItemFullRead, SystemItemRead
)
from app.utils.update_create_items import update_single_parent_size
from app.utils.get_item_response import create_nested_response

router = APIRouter()


@router.post(
    '/imports', status_code=HTTPStatus.OK
)
async def import_folders_and_files(
        items_data: SystemItemListCreate,
        session: AsyncSession = Depends(get_async_session),
) -> None:
    check_items_package_unique_id(items_data.items)
    check_date_is_valid(items_data.date)

    return {'Hello': 'FastAPI'}


@router.delete(
    '/delete/{id}', status_code=HTTPStatus.OK,
)
async def delete_folder_or_file(
        id: str,
        date: str = Query(
            regex=DATE_ISO_ZULU_FORMAT_REGEX,
            title='Date in ISO format',
            description='Date in ISO format',
            example='2020-12-31T21:00:00.223Z'
        ),
        session: AsyncSession = Depends(get_async_session),
):
    date = parse_and_check_date(date)
    item = await try_get_object_by_attribute(
        system_item_crud,
        attr_name='id', attr_value=id,
        session=session
    )
    check_date_is_valid(item.date, date)
    removed_item = await system_item_crud.remove(item, session)
    if removed_item.parent_id is not None:
        await update_single_parent_size(
            parent_id=removed_item.parent_id,
            date=date,
            session=session,
            commit=True
        )


@router.get(
    '/nodes/{id}',
    status_code=HTTPStatus.OK,
    response_model=SystemItemFullRead
)
async def get_item(
        id: str,
        session: AsyncSession = Depends(get_async_session),
):
    item = await try_get_object_by_attribute(
        system_item_crud,
        attr_name='id', attr_value=id, session=session
    )
    return await create_nested_response(session, item)


@router.get(
    '/updates',
    status_code=HTTPStatus.OK,
    response_model=List[SystemItemRead],
    deprecated=True
)
async def get_items_change_statistic(
        date: str = Query(
            regex=DATE_ISO_ZULU_FORMAT_REGEX,
            title='Date in ISO format',
            description='Date in ISO format',
            example='2020-12-31T21:00:00.223Z'
        ),
        session: AsyncSession = Depends(get_async_session)
):
    return None


@router.get(
    '/updates',
    status_code=HTTPStatus.OK,
    response_model=List[SystemItemRead],
    deprecated=True
)
async def get_items_change_statistic(
        date: str = Query(
            regex=DATE_ISO_ZULU_FORMAT_REGEX,
            title='Date in ISO format',
            description='Date in ISO format',
            example='2020-12-31T21:00:00.223Z'
        ),
        session: AsyncSession = Depends(get_async_session)
):
    return None


@router.get(
    '/node/{id}/history',
    status_code=HTTPStatus.OK,
    deprecated=True
)
async def get_history_item_change(
        id: str,
        date_start: Optional[str] = Query(
            None,
            regex=DATE_ISO_ZULU_FORMAT_REGEX,
            title='Date in ISO format',
            description='Date in ISO format',
            example='2020-12-31T21:00:00.223Z',
            alias='dateStart'
        ),
        date_end: Optional[str] = Query(
            None,
            regex=DATE_ISO_ZULU_FORMAT_REGEX,
            title='Date in ISO format',
            description='Date in ISO format',
            example='2020-12-31T21:00:00.223Z',
            alias='dateStart'
        ),
        session: AsyncSession = Depends(get_async_session)
):
    return None