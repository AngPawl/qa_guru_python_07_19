import requests
import jsonschema

from tests.conftest import base_url
from utils import load_schema


def test_status_code_is_ok():
    response = requests.get(f'{base_url}/users', params={'page': 1})

    assert (
        response.status_code == 200
    ), f"Status code {response.status_code} is incorrect"


def test_schema_is_valid():
    schema = load_schema('get_users.json')

    response = requests.get(f'{base_url}/users', params={'per_page': 1})

    jsonschema.validate(response.json(), schema)


def test_response_with_per_page_param_is_valid():
    response = requests.get(f'{base_url}/users', params={'page': 1, 'per_page': 3})

    assert (
        response.json()['per_page'] == 3
    ), f"Per page param returned incorrect value: {response.json()['per_page']}"


def test_response_time_is_valid():
    response = requests.get(f'{base_url}/users', params={'page': 1, 'per_page': 3})

    assert (
        response.elapsed.total_seconds() < 1
    ), f"Actual response time {response.elapsed.total_seconds()} is more than 1 second"


def test_headers_are_valid():
    response = requests.get(f'{base_url}/users', params={'page': 1})

    assert response.headers, "Response headers are empty"
    assert (
        response.headers['Content-Type'] == 'application/json; charset=utf-8'
    ), f"Header Content-Type value is incorrect: {response.headers['Content-Type']}"
    assert (
        response.headers['Connection'] == 'keep-alive'
    ), f"Header Connection value is incorrect: {response.headers['Connection']}"
    assert (
        response.headers['Cache-Control'] == 'max-age=14400'
    ), f"Header Cache-Control value is incorrect: {response.headers['Cache-Control']}"
    assert (
        response.headers['Access-Control-Allow-Origin'] == '*'
    ), f"Header Access-Control-Allow-Origin value is incorrect: {response.headers['Access-Control-Allow-Origin']}"
