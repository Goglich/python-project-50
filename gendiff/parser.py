import yaml
import json


def files_parser(file1, file2):
    if file1.endswith('.json') and file2.endswith('.json'):
        with open(file1, 'r') as fp:
            data1 = json.load(fp)
        with open(file2, 'r') as fp:
            data2 = json.load(fp)
    elif file1.endswith('.yaml') and file2.endswith('.yaml'):
        with open(file1, 'r') as fp:
            data1 = yaml.safe_load(fp)
        with open(file2, 'r') as fp:
            data2 = yaml.safe_load(fp)

    sorted_data1 = dict(sorted(data1.items()))
    sorted_data2 = dict(sorted(data2.items()))

    return sorted_data1, sorted_data2