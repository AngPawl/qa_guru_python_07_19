import jsonschema
import requests

from tests.conftest import base_url, register_new_valid_user, register_new_invalid_user
from utils import load_schema


def test_successful_registration():
    schema = load_schema('register_user.json')

    response = requests.post(
        url=f'{base_url}/register',
        json=register_new_valid_user,
    )

    jsonschema.validate(response.json(), schema)
    assert (
        response.status_code == 200
    ), f"Status code {response.status_code} is incorrect"


def test_unsuccessful_registration():
    response = requests.post(url=f'{base_url}/register', json=register_new_invalid_user)

    assert (
        response.status_code == 400
    ), f"Status code {response.status_code} is incorrect"
    assert (
        response.json()['error'] == 'Missing password'
    ), f"Error message {response.json()['error']} is incorrect"
