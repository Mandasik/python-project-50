import pytest
from gendiff.format_pkg.plain_format import plain, standardizes_value
from gendiff.format_pkg.stylish_format import (
    stylish,
    analyzes_node,
    routes_analysis,
    get_line,
    expands_dir_node,
)
from gendiff.format_pkg.json_format import json_f
from tests.fixtures.internal_representacion import INTERNAL_REPRESENTACION


NODE_1 = "      + follow: false"
NODE_2 = "      - setting3: true"
NODE_NONE = "      + setting3: null"
NODE_E = "        setting1: V 1"
NODE_N = "\n".join(["      - setting3: true", "      + setting3: null"])
NODE_NOT_EQUAL_DIR = "\n".join(
    [
        "      - nest: {",  # NOQA E122
        "            key: value",  # NOQA E122
        "        }",  # NOQA E122
        "      + nest: str",  # NOQA E122
    ]
)
NODE_DIR1 = "\n".join(
    [
        "        deep: {",  # NOQA E122
        "            id: 45",  # NOQA E122
        "        }",  # NOQA E122
    ]
)
NODE_DIR2 = "            id: 45"


@pytest.mark.parametrize(
    "path, func",
    [
        ("tests/fixtures/diff_f1_f2_json.txt", stylish),
        ("tests/fixtures/plain_diff.txt", plain),
        ("tests/fixtures/diff_json.txt", json_f),
        ("tests/fixtures/analyzes_node.txt", analyzes_node),
    ],
)
def test_combined_functions(path, func):
    with open(path, "r") as example:
        fp = example.read()
    assert fp == func(INTERNAL_REPRESENTACION)


@pytest.mark.parametrize(
    "value_correct, value",
    [
        ("null", None),
        ("true", True),
        ("2", 2),
        ("'coza-nostra'", "coza-nostra"),
        ("[complex value]", {"a": "gwe"}),
    ],
)
def test_standardizes_value(value_correct, value):
    assert value_correct == standardizes_value(value)


@pytest.mark.parametrize(
    "correct_out ,arg1, arg2, arg3, arg4, arg5, func",
    [
        (
            NODE_1,
            "follow",
            {"second": False},
            "only_2",
            2,
            "leaf",
            routes_analysis
        ),
        (
            NODE_2,
            "setting3",
            {"first": True},
            "only_1",
            2,
            "leaf",
            routes_analysis
        ),
        (
            NODE_E,
            "setting1",
            {"first": "V 1"},
            "equal",
            2,
            "leaf",
            routes_analysis
        ),
        (
            NODE_N,
            "setting3",
            {"first": True, "second": None},
            "not_equal",
            2,
            "leaf",
            routes_analysis,
        ),
        (
            NODE_NOT_EQUAL_DIR,
            "nest",
            {"first": {"key": "value"}, "second": "str"},
            "not_equal",
            2,
            "dir",
            routes_analysis,
        ),
        (NODE_1, "follow", False, "+", 2, "leaf", get_line),
        (NODE_NONE, "setting3", None, "+", 2, "leaf", get_line),
        (NODE_E, "setting1", "V 1", " ", 2, "leaf", get_line),
        (NODE_DIR1, "deep", {"id": 45}, " ", 2, "dir", get_line)
    ],
)
def test_constituent_function(correct_out, arg1, arg2, arg3, arg4, arg5, func):
    assert correct_out == func(arg1, arg2, arg3, arg4, arg5)


def test_expands_dir_node():
    assert NODE_DIR2 == expands_dir_node({"id": 45}, 3)
