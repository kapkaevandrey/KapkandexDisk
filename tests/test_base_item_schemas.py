from app.schemas.system_item import SystemItemCreate
from app.models.abstract_base import SystemItemType


def test_create_valid_schemas_no_date(
        system_item_folder_valid,
        system_item_file_valid,
):
    try:
        SystemItemCreate(
            **system_item_folder_valid
        )
        SystemItemCreate(
            **system_item_file_valid
        )
    except Exception as error:
        raise AssertionError(
            f'cannot create System Items base error - '
            f'{error}'
        )


def test_create_invalid_schemas_folder_no_date(
        system_item_folder_valid,
):
    invalid_params = dict(url='abc', size=2)
    for key, value in invalid_params.items():
        invalid_copy = system_item_folder_valid.copy()
        invalid_copy[key] = value
        try:
            SystemItemCreate(
                **invalid_copy
            )
            raise AssertionError(
                f'SystemItem schemas with type FOLDER cant have '
                f'field {key} with value {value}'
            )
        except:
            pass


def test_create_invalid_schemas_file_no_date(
        system_item_file_valid,
):
    invalid_params = dict(url=None, size=0)
    for key, value in invalid_params.items():
        invalid_copy = system_item_file_valid.copy()
        invalid_copy[key] = value
        try:
            SystemItemCreate(
                **invalid_copy
            )
            raise AssertionError(
                f'SystemItem schemas with type FILE cant have '
                f'field {key} with value {value}'
            )
        except:
            pass
