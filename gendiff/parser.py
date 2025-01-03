import yaml
import json
import os


def read_file(filepath):
    _, extension = os.path.splitext(filepath)
    extension = extension.lower()
    with open(filepath, 'r') as file:
        data = file.read()
    return parse_data(data, extension)


def parse_data(data, extension):
    if extension == '.json':
        return json.loads(data)
    if extension == '.yaml':
        return yaml.safe_load(data)
    if extension == '.yml':
        return yaml.safe_load(data)
    else:
        raise ValueError
