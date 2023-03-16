from gendiff import generate_diff
from gendiff.gendiff_module import *


def test_norm_gen_diff():
    with open('tests/fixtures/flat_json.txt', 'r') as correct:
        assert correct.read() == generate_diff('file1.json', 'file2.json')


def test_str_rec():
    file1 = {"c": 1, "b": 50, 'a': 3}
    file2 = {"c": 1, "b": 0, "d": 50}
    assert 'c: 1' == get_str_rec(file1, file2, 'c')
    assert ('- b: 50', '+ b: 0') == get_str_rec(file1, file2, 'b')
    assert '+ d: 50' == get_str_rec(file1, file2, 'd')
    assert '- a: 3' == get_str_rec(file1, file2, 'a')


def test_get_dict():
    dict_ = {"host": "hexlet.io", "timeout": 50,
             "proxy": "123.234.53.22", "follow": False}
    assert dict_ == get_dict_from_json('file1.json')
