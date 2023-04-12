import pytest
from gendiff.diff_pkg.gendiff_module import (
    get_format,
    get_dict,
    status_of_node,
    get_tree,
    value_of_leaf,
    get_node,
    type_of_node,
    generate_diff,
)


DICT_FROM_JSON = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"key": "value", "doge": {"wow": ""}},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
}
DICT_FROM_YAML = {"name": "John", "age": 28, "occupat": "Engineer"}
DICT_FROM_YML = {"name": "Jo", "age": 28, "oc": "Engineer"}
DICT2 = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {"key5": "value5"},
        "setting6": {"key": "value", "ops": "vops", "doge": {"wow": "so much"}},
    },
    "group1": {"foo": "bar", "baz": "bars", "nest": "str"},
    "group3": {"deep": {"id": {"number": 45}}, "fee": 100500},
}


@pytest.mark.parametrize(
    "format_out, path_correct",
    [
        ("stylish", "tests/fixtures/diff_f1_f2_json.txt"),
        ("plain", "tests/fixtures/plain_diff.txt"),
        ("json", "tests/fixtures/diff_json.txt"),
    ],
)
def test_generate_diff(format_out, path_correct):
    path1 = "tests/fixtures/file1.JSON"
    path2 = "tests/fixtures/file2.json"
    with open(path_correct, "r") as fp:
        assert fp.read() == generate_diff(path1, path2, format_out)
    assert "This format is not supported" == generate_diff(
        path1, path2, "surprise"
    )


@pytest.mark.parametrize(
    "correct, path, func",
    [
        (".json", "tests/fixtures/file1.JSON", get_format),
        (DICT_FROM_JSON, "tests/fixtures/file1.JSON", get_dict),
        ("not supported", "tests/fixtures/flat_jaml.txt", get_dict),
        (DICT_FROM_YAML, "tests/fixtures/file_one.yml", get_dict),
    ],
)
def test_read_get_dict(correct, path, func):
    assert correct == func(path)


@pytest.mark.parametrize(
    "correct, func, arg1, arg2, arg3",
    [
        ("dir", type_of_node, DICT_FROM_JSON, DICT2, "common"),
        ("leaf", type_of_node, DICT_FROM_JSON, DICT2, "setting2"),
        ("equal", status_of_node, DICT_FROM_YAML, DICT_FROM_YML, "age"),
        ("not_equal", status_of_node, DICT_FROM_YAML, DICT_FROM_YML, "name"),
        ("only_1", status_of_node, DICT_FROM_YAML, DICT_FROM_YML, "occupat"),
        ("only_2", status_of_node, DICT_FROM_YAML, DICT_FROM_YML, "oc"),
    ],
)
def test_type_of_node_and_status(correct, func, arg1, arg2, arg3):
    assert correct == func(arg1, arg2, arg3)


@pytest.mark.parametrize(
    "correct, arg1, arg2, arg3, arg4",
    [
        (
            {"first": DICT_FROM_JSON["common"]["setting1"]},
            DICT_FROM_JSON["common"],
            DICT2["common"],
            "setting1",
            "equal",
        ),
        (
            {"first": DICT_FROM_JSON["common"]["setting1"]},
            DICT_FROM_JSON["common"],
            DICT2["common"],
            "setting1",
            "only_1",
        ),
        (
            {
                "first": DICT_FROM_JSON["common"]["setting3"],
                "second": DICT2["common"]["setting3"],
            },
            DICT_FROM_JSON["common"],
            DICT2["common"],
            "setting3",
            "not_equal",
        ),
        (
            {"second": DICT2["common"]["follow"]},
            DICT_FROM_JSON["common"],
            DICT2["common"],
            "follow",
            "only_2",
        ),
    ],
)
def test_value_of_leaf(correct, arg1, arg2, arg3, arg4):
    assert correct == value_of_leaf(arg1, arg2, arg3, arg4)


def test_get_node():
    assert {
        "name": "common",
        "status": "nested",
        "chieldren": ["setting1", 200, "setting3", "setting6"],
    } == get_node(
        "common", "nested", chieldren=["setting1", 200, "setting3", "setting6"]
    )
    assert {
        "name": "setting1",
        "node_type": "leaf",
        "status": "equal",
        "value": "Value 1",
    } == get_node("setting1", "equal", type_node="leaf", value="Value 1")


def test_get_tree():
    with open("tests/fixtures/test_get_tree.txt", "r") as fp:
        assert fp.read() == str(get_tree(DICT_FROM_JSON, DICT2))
