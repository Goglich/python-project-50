from gendiff import parser
from gendiff.formater import stylish, json, plain
from gendiff.gendiff import get_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = parser.read_file(file_path1), parser.read_file(file_path2)
    diff = get_diff(data1, data2)

    if format_name == 'plain':
        return plain.format(diff)
    elif format_name == 'json':
        return json.format(diff)
    elif format_name == 'stylish':
        return stylish.format(diff)

