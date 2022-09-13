from datetime import datetime

from dateutil import tz
import pytest



@pytest.fixture()
def system_item_folder_valid():
    return dict(
        id='my_folder_id',
        url=None, parent_id=None, type='FOLDER',
        size=None
    )


@pytest.fixture()
def system_item_file_valid():
    return dict(
        id='my_file_id',
        url='/file/', parent_id=None, type='FILE',
        size=123
    )
