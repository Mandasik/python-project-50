from gendiff.format_pkg import plain_format
from tests.fixtures.internal_representacion import INTERNAL_REPRESENTACION


def test_plain():
    with open("tests/fixtures/plain_diff.txt", "r") as example:
        p = example.read()
    assert p == plain_format.plain(INTERNAL_REPRESENTACION)