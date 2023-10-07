import jsonschema
import requests

from tests.conftest import base_url, post_new_user
from utils import load_schema


def test_status_code_is_ok():
    response = requests.post(url=f'{base_url}/users', json=post_new_user)

    assert (
        response.status_code == 201
    ), f"Status code {response.status_code} is incorrect"


def test_schema_is_valid():
    schema = load_schema('post_user.json')

    response = requests.post(url=f'{base_url}/users', json=post_new_user)

    jsonschema.validate(response.json(), schema)


def test_response_data_is_valid():
    response = requests.post(url=f'{base_url}/users', json=post_new_user)

    assert (
        response.json()['name'] == post_new_user['name']
    ), f"Response data contains incorrect data: {response.json()['name']}"
    assert (
        response.json()['job'] == post_new_user['job']
    ), f"Response data contains incorrect data: {response.json()['job']}"
