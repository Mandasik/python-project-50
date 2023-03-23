from gendiff.diff_pkg.gendiff_module import get_format, get_dict, type_of_leaf
from gendiff.diff_pkg.gendiff_module import get_tree, value_of_leaf, get_node


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


def test_generate_diff():
    pass


def test_read_get_dict():
    assert ".json" == get_format("tests/fixtures/file1.JSON")
    assert DICT_FROM_JSON == get_dict("tests/fixtures/file1.JSON")
    assert "not supported" == get_dict("tests/fixtures/flat_jaml.txt")
    assert DICT_FROM_YAML == get_dict("tests/fixtures/file_one.yml")


def test_type_of_node():
    assert "equal" == type_of_leaf(DICT_FROM_YAML, DICT_FROM_YML, "age")
    assert "not equal" == type_of_leaf(DICT_FROM_YAML, DICT_FROM_YML, "name")
    assert "only 1" == type_of_leaf(DICT_FROM_YAML, DICT_FROM_YML, "occupat")
    assert "only 2" == type_of_leaf(DICT_FROM_YAML, DICT_FROM_YML, "oc")


def test_value_of_leaf():
    assert {"first": DICT_FROM_JSON["common"]["setting1"]} == value_of_leaf(
        DICT_FROM_JSON["common"], DICT2["common"], "setting1", "equal"
    )
    assert {"first": DICT_FROM_JSON["common"]["setting1"]} == value_of_leaf(
        DICT_FROM_JSON["common"], DICT2["common"], "setting1", "only 1"
    )
    assert {
        "first": DICT_FROM_JSON["common"]["setting3"],
        "second": DICT2["common"]["setting3"],
    } == value_of_leaf(
        DICT_FROM_JSON["common"], DICT2["common"], "setting3", "not equal"
    )
    assert {"second": DICT2["common"]["follow"]} == value_of_leaf(
        DICT_FROM_JSON["common"], DICT2["common"], "follow", "only 2"
    )


def test_get_node():
    assert {
        "name": "common",
        "node type": "dir",
        "chieldren": ["setting1", 200, "setting3", "setting6"],
    } == get_node("common", "dir",
                  chieldren=["setting1", 200, "setting3", "setting6"])
    assert {
        'name': "setting1",
        'node type': "equal",
        'value': "Value 1"}


def test_get_tree():
    with open("tests/fixtures/test_get_tree.txt", "r") as fp:
        assert fp.read() == str(get_tree(DICT_FROM_JSON, DICT2))
