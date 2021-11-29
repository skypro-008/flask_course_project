def send_form_request(test_client, method: str, url: str, json_data: dict):
    return getattr(test_client, method)(
        url, data='&'.join([f'{k}={v}' for k, v in json_data.items()]),
        content_type="application/x-www-form-urlencoded"
    )
