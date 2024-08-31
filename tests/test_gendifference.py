from gendiff.module import gendiff
from tests.fixtures.fixrute_paths import FILE1_JSON, FILE2_JSON

def excepted_result():
        return '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

def test_of_the_test():
    excepted = excepted_result()
    diff = gendiff.generate_diff(FILE1_JSON, FILE2_JSON)
    assert diff == excepted
