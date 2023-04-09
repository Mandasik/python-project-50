from gendiff.format_pkg import json_format
from tests.fixtures.internal_representacion import INTERNAL_REPRESENTACION


def test_json():
    with open("tests/fixtures/diff_json.txt", "r") as example:
        fp = example.read()
    assert fp == json_format.json_f(INTERNAL_REPRESENTACION)