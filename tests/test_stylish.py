from gendiff.format_pkg import stylish_format
from tests.fixtures.internal_representacion import INTERNAL_REPRESENTACION


NODE_1 = "      + follow: false"
NODE_2 = "      - setting3: true"
NODE_NONE = "      + setting3: null"
NODE_EMPTY = "      + setting3:"
NODE_EQUAL = "        setting1: Value 1"
NODE_NOT_EQUAL = "\n".join(["      - setting3: true", "      + setting3: null"])
NODE_NOT_EQUAL_DIR = "\n".join(
    [
    "      - nest: {",
    "            key: value",
    "        }",
    "      + nest: str"
    ]
)
NODE_DIR1 = "\n".join(
    [
    "        deep: {",
    "            id: 45",
    "        }",
    ]
)
NODE_DIR2 = "            id: 45"


def test_stylish():
    with open("tests/fixtures/diff_f1_f2_json.txt", "r") as example:
        p = example.read()
    assert p == stylish_format.stylish(INTERNAL_REPRESENTACION)


def test_analyzes_node():
    with open("tests/fixtures/analyzes_node.txt", "r") as example:
        p = example.read()
    assert p == stylish_format.analyzes_node(INTERNAL_REPRESENTACION)


def test_routes_analysis():
    assert NODE_1 == stylish_format.routes_analysis(
        "follow", {"second": False}, "only_2", 2, "leaf"
    )
    assert NODE_2 == stylish_format.routes_analysis(
        "setting3", {"first": True}, "only_1", 2, "leaf"
    )
    assert NODE_EQUAL == stylish_format.routes_analysis(
        "setting1", {"first": "Value 1"}, "equal", 2, "leaf"
    )
    assert NODE_NOT_EQUAL == stylish_format.routes_analysis(
        "setting3", {"first": True, "second": None}, "not_equal", 2
    )
    assert NODE_NOT_EQUAL_DIR == stylish_format.routes_analysis(
        "nest", {"first": {"key": "value"}, "second": "str"}, "not_equal", 2
    )


def test_get_line():
    assert NODE_1 == stylish_format.get_line(
        "follow", False, "+", 2, "leaf"
    )
    assert NODE_NONE == stylish_format.get_line(
        "setting3", None, "+", 2, "leaf"
    )
    assert NODE_EMPTY == stylish_format.get_line(
        "setting3", "", "+", 2, "leaf"
    )
    assert NODE_EQUAL == stylish_format.get_line(
        "setting1", "Value 1", " ", 2, "leaf"
    )
    assert NODE_DIR1 == stylish_format.get_line(
        "deep", {"id": 45}, " ", 2, "dir"
    )


def test_expands_dir_node():
    assert NODE_DIR2 == stylish_format.expands_dir_node({"id": 45}, 3)
