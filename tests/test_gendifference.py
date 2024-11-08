from gendiff.generate_diff import generate_diff
from tests.fixtures import fixture_paths
import pytest


def excepted_result(path):
    with (open(path)) as file:
        result = file.read()
        return result


small_files = excepted_result('tests/fixtures/excepted_result.txt')
big_files = excepted_result('tests/fixtures/excepted_result_nested.txt')
plain = excepted_result('tests/fixtures/excepted_result_plain.txt')
json = excepted_result('tests/fixtures/excepted_result_json.txt')


@pytest.mark.parametrize("path1, path2, style, expected", [
    (fixture_paths.FILE1_JSON, fixture_paths.FILE2_JSON, 'stylish', small_files),
    (fixture_paths.FILE1_YAML, fixture_paths.FILE2_YAML, 'stylish', small_files),
    (fixture_paths.FILE1_YML, fixture_paths.FILE2_YML, 'stylish', small_files),
    (fixture_paths.FILE3_JSON, fixture_paths.FILE4_JSON, 'stylish', big_files),
    (fixture_paths.FILE3_YAML, fixture_paths.FILE4_YAML, 'stylish', big_files),
    (fixture_paths.FILE3_JSON, fixture_paths.FILE4_JSON, 'plain', plain),
    (fixture_paths.FILE3_YAML, fixture_paths.FILE4_YAML, 'plain', plain),
    (fixture_paths.FILE3_JSON, fixture_paths.FILE4_JSON, 'json', json),
    (fixture_paths.FILE3_YAML, fixture_paths.FILE4_YAML, 'json', json)
])
def test_all(path1, path2, style, expected):
    assert generate_diff(path1, path2, style) == expected
