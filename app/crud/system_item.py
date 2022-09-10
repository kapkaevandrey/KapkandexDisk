from app.models import SystemItem
from app.schemas.system_item import SystemItemCreate, SystemItemUpdate
from app.crud.base import BaseCRUD

system_item_crud = BaseCRUD[
    SystemItem, SystemItemCreate, SystemItemUpdate
](SystemItem)
