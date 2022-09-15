import pytest


@pytest.mark.parametrize('json', [
    {
        "items": [{"id": "root1", "url": None, "parentId": None, "size": None, "type": "FOLDER"}],
        "updateDate": '2025-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "root1", "url": 'file', "parentId": None, "size": None, "type": "FOLDER"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "root1", "url": None, "parentId": 'fsdfs', "size": None, "type": "FOLDER"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "root1", "url": None, "parentId": None, "size": 100, "type": "FOLDER"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
]
                         )
def test_import_test_invalid_test_package_folder(
        test_client, json
):
    response = test_client.post(f'/imports', json=json)
    assert response.status_code == 400, (
        f'status code must be 400 when validation failed {json}'
    )


@pytest.mark.parametrize('json', [
    {
        "items": [{"id": "file1", "url": '/file1', "parentId": None, "size": 0, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "file1", "url": '/file1', "parentId": None, "size": -5, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "file1", "url": '/file1', "parentId": None, "size": 1, "type": "FILE"}],
        "updateDate": '2025-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "", "url": '/file1', "parentId": None, "size": 1, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "file1", "url": '', "parentId": None, "size": 1, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "file1", "url": 'time_to_drink/', "parentId": None, "size": 1, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "file1", "url": '/file1', "parentId": 'HarryPotter', "size": 1, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
    {
        "items": [{"id": "file1", "url": '/file1', "parentId": None, "size": None, "type": "FILE"}],
        "updateDate": '2022-06-28T21:12:01Z'
    },
]
                         )
def test_import_test_invalid_test_package_file(
        test_client, json
):
    response = test_client.post(f'/imports', json=json)
    assert response.status_code == 400, (
        f'status code must be 400 when validation failed {json}'
    )


def test_response_mini_package(
        test_client, item_mini_package, response_mini_package
):
    test_client.post(f'/imports', json=item_mini_package)
    root_id = response_mini_package['id']
    response = test_client.get(f'nodes/{root_id}')
    assert response.status_code == 200, (
        f'status code must be 200 when success'
    )
    assert response.json() == response_mini_package, 'Bad response'
    for val, item in enumerate(response_mini_package['children']):

        response = test_client.get(f'nodes/{item["id"]}')
        assert response.status_code == 200, (
            f'status code must be 200 when success'
        )
        assert response.json() == item, 'Bad response'


def test_response_shuffle_package(
        test_client, shuffle_item_package, response_shuffle_item_package
):
    test_client.post(f'/imports', json=shuffle_item_package)

    root_id = response_shuffle_item_package['id']
    response = test_client.get(f'nodes/{root_id}')
    assert response.status_code == 200, (
        f'status code must be 200 when success'
    )
    assert response.json() == response_shuffle_item_package, 'Bad response'


def test_response_package_with_many_folders(
        test_client, item_package_with_many_folders, response_package_with_many_folders
):
    test_client.post(f'/imports', json=item_package_with_many_folders)

    root_id = response_package_with_many_folders['id']
    response = test_client.get(f'nodes/{root_id}')
    assert response.status_code == 200, (
        f'status code must be 200 when success'
    )
    assert response.json() == response_package_with_many_folders, 'Bad response'


def test_change_item_type(
        test_client, item_mini_package, update_date_str
):
    test_client.post(f'/imports', json=item_mini_package)
    update_package = {
        'items': [
            {
                "id": "root1",
                "url": None,
                "parentId": None,
                "size": None,
                "type": "FILE"
            }
        ],
        'updateDate': update_date_str
    }
    response = test_client.post(f'/imports', json=update_package)
    assert response.status_code == 400, (
        f'status code must be 400 when we try change type'
    )
    update_package = {
        'items': [
            {
                "id": "file1_1",
                "url": "/file/1_1",
                "parentId": "root1",
                "size": 15,
                "type": "FOLDER"
            }
        ],
        'updateDate': update_date_str
    }
    response = test_client.post(f'/imports', json=update_package)
    assert response.status_code == 400, (
        f'status code must be 400 when we try change type'
    )


def test_change_folder_params(
        test_client, item_mini_package, update_date_str
):
    test_client.post(f'/imports', json=item_mini_package)
    invalid_date = {"size": 10, "url": "/folder"}
    for key, value in invalid_date.items():
        root = item_mini_package["items"][0]
        root[key] = value
        package = {"items": [root], "updateDate": update_date_str}
        response = test_client.post(f'/imports', json=package)
        assert response.status_code == 400, (
            f'status code must be 400 when we try change folder size or url'
        )
