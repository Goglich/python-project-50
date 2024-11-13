from gendiff.generate_diff import generate_diff
from tests.fixtures import fixture_paths
import pytest


def excepted_result(path):
    with (open(path)) as file:
        result = file.read()
        return result


@pytest.mark.parametrize("path1, path2, style, expected", [
    (fixture_paths.FILE1_JSON,
     fixture_paths.FILE2_JSON,
     'stylish',
     'tests/fixtures/excepted_result.txt'),
    (fixture_paths.FILE1_YAML,
     fixture_paths.FILE2_YAML,
     'stylish',
     'tests/fixtures/excepted_result.txt'),
    (fixture_paths.FILE1_YML,
     fixture_paths.FILE2_YML,
     'stylish',
     'tests/fixtures/excepted_result.txt'),
    (fixture_paths.FILE3_JSON,
     fixture_paths.FILE4_JSON,
     'stylish',
     'tests/fixtures/excepted_result_nested.txt'),
    (fixture_paths.FILE3_YAML,
     fixture_paths.FILE4_YAML,
     'stylish',
     'tests/fixtures/excepted_result_nested.txt'),
    (fixture_paths.FILE3_JSON,
     fixture_paths.FILE4_JSON,
     'plain',
     'tests/fixtures/excepted_result_plain.txt'),
    (fixture_paths.FILE3_YAML,
     fixture_paths.FILE4_YAML,
     'plain',
     'tests/fixtures/excepted_result_plain.txt'),
    (fixture_paths.FILE3_JSON,
     fixture_paths.FILE4_JSON,
     'json',
     'tests/fixtures/excepted_result_json.txt'),
    (fixture_paths.FILE3_YAML,
     fixture_paths.FILE4_YAML,
     'json',
     'tests/fixtures/excepted_result_json.txt')
])
def test_generate_diff(path1, path2, style, expected_path):
    expected = excepted_result(expected_path)
    assert generate_diff(path1, path2, style) == expected
