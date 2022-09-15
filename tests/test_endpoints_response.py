def test_get_not_valid_id(test_client, not_found_response):
    node_id = 'BobaFet'
    response = test_client.get(f'/nodes/{node_id}')
    assert response.status_code == 404, (
        'status code must be 404 when we try get Non - existent'
        'item'
    )
    assert response.json() == not_found_response, 'Invalid response body'


def test_import_test_package(
        test_client, item_mini_package
):
    response = test_client.post(
        f'/imports', json=item_mini_package
    )
    assert response.status_code == 200, (
        'status code must be 200 when success'
    )


def test_delete_not_valid_id(
        test_client, not_found_response, update_date_str
):
    node_id = 'BobaFet'
    response = test_client.delete(
        f'/delete/{node_id}', params={'date': update_date_str}
    )
    assert response.status_code == 404, (
        'status code must be 404 when we try get non - existent'
        'item'
    )
    assert response.json() == not_found_response, 'Invalid response body'


def test_delete_not_valid_date(
        test_client, bad_request_response,
        invalid_update_date_str, item_mini_package
):
    response = test_client.post(
        f'/imports', json=item_mini_package
    )
    for item in item_mini_package['items']:
        response = test_client.delete(
            f'/delete/{item["id"]}', params={'date': invalid_update_date_str}
        )
        assert response.status_code == 400, (
            'status code must be 400 when we have invalid date'
        )
        assert response.json() == bad_request_response, 'Invalid response body'

