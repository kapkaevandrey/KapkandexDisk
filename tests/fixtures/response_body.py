import pytest


@pytest.fixture()
def not_found_response():
    return {'code': 404, 'message': 'Item not found'}


@pytest.fixture()
def bad_request_response():
    return {'code': 400, 'message': 'Validation Failed'}
