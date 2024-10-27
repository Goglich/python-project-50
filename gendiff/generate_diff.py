from gendiff import parser
from gendiff.formater import formater, json, plain
from gendiff.module.gendiff import get_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1, data2 = parser.files_parser(file_path1, file_path2)
    diff = get_diff(data1, data2)

    if format_name == 'plain':
        return plain.build_plain(diff)
    elif format_name == 'json':
        return json.make_json(diff)
    else:
        return formater.make_stylish(diff)
