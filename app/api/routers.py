from fastapi import APIRouter
from app.api.endpoints import system_item_router
from app.api.endpoints import system_item_history_router


main_router = APIRouter()
main_router.include_router(
    system_item_router,
    tags=['Folders and Files']
)
main_router.include_router(
    system_item_history_router,
    tags=['File modification statistics']
)
