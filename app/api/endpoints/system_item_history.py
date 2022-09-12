from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.constants import DATE_ISO_ZULU_FORMAT_REGEX
from app.schemas.system_item import SystemItemRead


router = APIRouter()


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
) -> None:
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
) -> None:
    return None
