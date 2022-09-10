from datetime import datetime
from typing import Optional
from http import HTTPStatus

from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.config import settings
from app.crud import system_item_crud


router = APIRouter()

