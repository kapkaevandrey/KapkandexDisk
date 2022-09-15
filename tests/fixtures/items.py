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
        url='/file', parent_id=None, type='FILE',
        size=123
    )


@pytest.fixture()
def item_one_folder_package(create_date_str):
    return {
        "items": [
            {
                "id": "root1",
                "url": None,
                "parentId": None,
                "size": None,
                "type": "FOLDER"
            }
        ],
        "updateDate": create_date_str
    }



@pytest.fixture()
def item_package_with_many_folders(create_date_str):
    return {
        "items": [
            {
                "id": "root3",
                "url": None,
                "parentId": None,
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root3_1",
                "url": None,
                "parentId": "root3",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root3_2",
                "url": None,
                "parentId": "root3",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root3_3",
                "url": None,
                "parentId": "root3",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root3_1_1",
                "url": None,
                "parentId": "root3_1",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "file3_1_1_1",
                "url": "/file",
                "parentId": "root3_1_1",
                "size": 35,
                "type": "FILE"
            },
        ],
        "updateDate": create_date_str
    }


@pytest.fixture()
def shuffle_item_package(create_date_str):
    return {
        "items": [
            {
                "id": "root2",
                "url": None,
                "parentId": None,
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root2_1",
                "url": None,
                "parentId": "root2",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root2_2",
                "url": None,
                "parentId": "root2",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root2_2_1",
                "url": None,
                "parentId": "root2_2",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "file2_1_1",
                "url": "/file/2_1_1",
                "parentId": "root2_1",
                "size": 20,
                "type": "FILE"
            },
            {
                "id": "file2_1_2",
                "url": "/file/2_1_2",
                "parentId": "root2_1",
                "size": 108,
                "type": "FILE"
            },
            {
                "id": "file2_1",
                "url": "/file/2_1",
                "parentId": "root2",
                "size": 14,
                "type": "FILE"
            },
            {
                "id": "file2_2_1",
                "url": "/file/2_2_2",
                "parentId": "root2_2",
                "size": 12,
                "type": "FILE"
            },
            {
                "id": "file2_2_1_1",
                "url": "/file/2_2_1_1",
                "parentId": "root2_2_1",
                "size": 25,
                "type": "FILE"
            }
        ],
        "updateDate": create_date_str
    }


@pytest.fixture()
def item_mini_package(create_date_str):
    return {
        "items": [
            {
                "id": "root1",
                "url": None,
                "parentId": None,
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "root1_1",
                "url": None,
                "parentId": "root1",
                "size": None,
                "type": "FOLDER"
            },
            {
                "id": "file1_1",
                "url": "/file/1_1",
                "parentId": "root1",
                "size": 15,
                "type": "FILE"
            }
        ],
        "updateDate": create_date_str
    }


@pytest.fixture()
def response_mini_package(create_date_str):
    return {
        "id": "root1",
        "url": None,
        "parentId": None,
        "type": "FOLDER",
        "size": 15,
        "date": create_date_str,
        "children": [
            {
                "id": "root1_1",
                "url": None,
                "parentId": "root1",
                "type": "FOLDER",
                "size": None,
                "date": create_date_str,
                "children": []
            },
            {
                "id": "file1_1",
                "url": "/file/1_1",
                "parentId": "root1",
                "type": "FILE",
                "size": 15,
                "date": create_date_str,
                "children": None
            }
        ]
    }


@pytest.fixture()
def response_shuffle_item_package(create_date_str):
    return {
        "id": "root2",
        "url": None,
        "parentId": None,
        "type": "FOLDER",
        "size": 179,
        "date": create_date_str,
        "children": [
            {
                "id": "root2_1",
                "url": None,
                "parentId": "root2",
                "type": "FOLDER",
                "size": 128,
                "date": create_date_str,
                "children": [
                    {
                        "id": "file2_1_1",
                        "url": "/file/2_1_1",
                        "parentId": "root2_1",
                        "type": "FILE",
                        "size": 20,
                        "date": create_date_str,
                        "children": None
                    },
                    {
                        "id": "file2_1_2",
                        "url": "/file/2_1_2",
                        "parentId": "root2_1",
                        "type": "FILE",
                        "size": 108,
                        "date": create_date_str,
                        "children": None
                    }
                ]
            },
            {
                "id": "root2_2",
                "url": None,
                "parentId": "root2",
                "type": "FOLDER",
                "size": 37,
                "date": create_date_str,
                "children": [
                    {
                        "id": "root2_2_1",
                        "url": None,
                        "parentId": "root2_2",
                        "type": "FOLDER",
                        "size": 25,
                        "date": create_date_str,
                        "children": [
                            {
                                "id": "file2_2_1_1",
                                "url": "/file/2_2_1_1",
                                "parentId": "root2_2_1",
                                "type": "FILE",
                                "size": 25,
                                "date": create_date_str,
                                "children": None
                            }
                        ]
                    },
                    {
                        "id": "file2_2_1",
                        "url": "/file/2_2_2",
                        "parentId": "root2_2",
                        "type": "FILE",
                        "size": 12,
                        "date": create_date_str,
                        "children": None
                    }
                ]
            },
            {
                "id": "file2_1",
                "url": "/file/2_1",
                "parentId": "root2",
                "type": "FILE",
                "size": 14,
                "date": create_date_str,
                "children": None
            }
        ]
    }


@pytest.fixture()
def response_package_with_many_folders(create_date_str):
    return {
        "id": "root3",
        "url": None,
        "parentId": None,
        "type": "FOLDER",
        "size": 35,
        "date": create_date_str,
        "children": [
            {
                "id": "root3_1",
                "url": None,
                "parentId": "root3",
                "type": "FOLDER",
                "size": 35,
                "date": create_date_str,
                "children": [
                    {
                        "id": "root3_1_1",
                        "url": None,
                        "parentId": "root3_1",
                        "type": "FOLDER",
                        "size": 35,
                        "date": create_date_str,
                        "children": [
                            {
                                "id": "file3_1_1_1",
                                "url": "/file",
                                "parentId": "root3_1_1",
                                "type": "FILE",
                                "size": 35,
                                "date": create_date_str,
                                "children": None
                            }
                        ]
                    }
                ]
            },
            {
                "id": "root3_2",
                "url": None,
                "parentId": "root3",
                "type": "FOLDER",
                "size": None,
                "date": create_date_str,
                "children": []
            },
            {
                "id": "root3_3",
                "url": None,
                "parentId": "root3",
                "type": "FOLDER",
                "size": None,
                "date": create_date_str,
                "children": []
            }
        ]
    }
