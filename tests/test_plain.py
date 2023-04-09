from gendiff.format_pkg import plain_format
from tests.fixtures.internal_representacion import INTERNAL_REPRESENTACION


def test_plain():
    with open("tests/fixtures/plain_diff.txt", "r") as example:
        p = example.read()
    assert p == plain_format.plain(INTERNAL_REPRESENTACION)


def test_standardizes_value():
    assert "null" == plain_format.standardizes_value(None)
    assert "true" == plain_format.standardizes_value(True)
    assert "2" == plain_format.standardizes_value(2)
    assert "'coza-nostra'" == plain_format.standardizes_value("coza-nostra")
    assert "[complex value]" == plain_format.standardizes_value({"a": "gwe"})
