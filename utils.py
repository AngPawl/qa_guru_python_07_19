import json
import os


def load_schema(name):
    current_dir = os.path.dirname(__file__)

    path = os.path.join(current_dir, 'json_schemes', name)

    with open(path) as file:
        json_schema = json.loads(file.read())

    return json_schema
