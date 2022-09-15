import pytest


@pytest.fixture()
def create_date_str():
    return "2022-05-28T21:12:01Z"


@pytest.fixture()
def update_date_str():
    return "2022-06-28T21:12:01Z"


@pytest.fixture()
def second_update_date_str():
    return "2022-06-28T21:12:01Z"
