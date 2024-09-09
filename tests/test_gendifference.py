from gendiff.module import gendiff
from gendiff import parser
from tests.fixtures.fixrute_paths import FILE1_JSON, FILE2_JSON, FILE1_YAML, FILE2_YAML

def excepted_result():
        return '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''


def test_get_diff_json():
    excepted = excepted_result()
    data1, data2 = parser.files_parser(FILE1_JSON, FILE2_JSON)
    diff = gendiff.generate_diff(data1, data2)
    assert diff == excepted

def test_get_diff_yaml():
    excepted = excepted_result()
    data1, data2 = parser.files_parser(FILE1_YAML, FILE2_YAML)
    diff = gendiff.generate_diff(data1, data2)
    assert diff == excepted