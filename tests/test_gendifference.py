from gendiff.generate_diff import generate_diff
from tests.fixtures.fixture_paths import FILE1_JSON, FILE2_JSON, FILE1_YAML, FILE2_YAML, FILE1_YML, FILE2_YML, FILE3_JSON, FILE4_JSON


def excepted_result(path):
    with (open(path)) as file:
        result = file.read()
        return result


def test_get_diff_json():
    excepted = excepted_result('tests/fixtures/excepted_result.txt')
    diff = generate_diff(FILE1_JSON, FILE2_JSON)
    assert diff == excepted


def test_get_diff_yaml():
    excepted = excepted_result('tests/fixtures/excepted_result.txt')
    diff = generate_diff(FILE1_YAML, FILE2_YAML)
    assert diff == excepted


def test_get_diff_yml():
    excepted = excepted_result('tests/fixtures/excepted_result.txt')
    diff = generate_diff(FILE1_YML, FILE2_YML)
    assert diff == excepted


def test_get_diff_nested_json():
    excepted = excepted_result('tests/fixtures/excepted_result_nested.txt')
    diff = generate_diff(FILE3_JSON, FILE4_JSON)
    assert diff == excepted


def test_get_diff_plain():
    excepted = excepted_result('tests/fixtures/excepted_result_plain.txt')
    diff = generate_diff(FILE3_JSON, FILE4_JSON, 'plain')
    assert diff == excepted

def test_get_diff_format_json():
    excepted = excepted_result('tests/fixtures/excepted_result_json.txt')
    diff = generate_diff(FILE3_JSON, FILE4_JSON, 'json')
    assert diff == excepted
