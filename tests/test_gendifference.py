from gendiff.module import gendiff
from gendiff.formater import formater
from gendiff.formater import plain
from gendiff.formater import json
from gendiff import parser
from tests.fixtures.fixture_paths import FILE1_JSON, FILE2_JSON, FILE1_YAML, FILE2_YAML, FILE3_JSON, FILE4_JSON


def excepted_result(path):
    with (open(path)) as file:
        result = file.read()
        return result


def test_get_diff_json():
    excepted = excepted_result('tests/fixtures/excepted_result.txt')
    data1, data2 = parser.files_parser(FILE1_JSON, FILE2_JSON)
    diff = formater.make_stylish(gendiff.generate_diff(data1, data2))
    assert diff == excepted


def test_get_diff_yaml():
    excepted = excepted_result('tests/fixtures/excepted_result.txt')
    data1, data2 = parser.files_parser(FILE1_YAML, FILE2_YAML)
    diff = formater.make_stylish(gendiff.generate_diff(data1, data2))
    assert diff == excepted


def test_get_diff_nested_json():
    excepted = excepted_result('tests/fixtures/excepted_result_nested.txt')
    data1, data2 = parser.files_parser(FILE3_JSON, FILE4_JSON)
    diff = formater.make_stylish(gendiff.generate_diff(data1, data2))
    assert diff == excepted


def test_get_diff_plain():
    excepted = excepted_result('tests/fixtures/excepted_result_plain.txt')
    data1, data2 = parser.files_parser(FILE3_JSON, FILE4_JSON)
    diff = plain.build_plain(gendiff.generate_diff(data1, data2))
    assert diff == excepted

def test_get_diff_format_json():
    excepted = excepted_result('tests/fixtures/excepted_result_json.txt')
    data1, data2 = parser.files_parser(FILE3_JSON, FILE4_JSON)
    diff = json.make_json(gendiff.generate_diff(data1, data2))
    assert diff == excepted
