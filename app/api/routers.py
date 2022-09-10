from fastapi import APIRouter
from app.api.endpoints import system_item_router


main_router = APIRouter()
main_router.include_router(
    system_item_router,
    tags=['Folders and Files']
)
