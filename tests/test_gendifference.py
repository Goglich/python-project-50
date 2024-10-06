from gendiff.module import gendiff
from gendiff.formater import formater
from gendiff import parser
from tests.fixtures.fixrute_paths import FILE1_JSON, FILE2_JSON, FILE1_YAML, FILE2_YAML, FILE3_JSON, FILE4_JSON

def excepted_result():
        return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

def excepted_result_nested():
        return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

def test_get_diff_json():
    excepted = excepted_result()
    data1, data2 = parser.files_parser(FILE1_JSON, FILE2_JSON)
    diff = formater.make_stylish(gendiff.generate_diff(data1, data2))
    assert diff == excepted

def test_get_diff_yaml():
    excepted = excepted_result()
    data1, data2 = parser.files_parser(FILE1_YAML, FILE2_YAML)
    diff = formater.make_stylish(gendiff.generate_diff(data1, data2))
    assert diff == excepted

def test_get_diff_nested_json():
    excepted = excepted_result_nested()
    data1, data2 = parser.files_parser(FILE3_JSON, FILE4_JSON)
    diff = formater.make_stylish(gendiff.generate_diff(data1, data2))
    assert diff == excepted