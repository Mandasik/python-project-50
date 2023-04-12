from json import dumps
from gendiff.format_pkg.constans import (
    ONLY_1, ONLY_2, NOT_EQUAL, NESTED
)


def plain(tree, path=""):
    result = []
    for node in tree:
        status = node["status"]
        name = node["name"]
        name = path + "." + node["name"] if path else node["name"]
        value = node.get("value")
        if status == ONLY_2:
            result.append(
                (
                    f"Property '{name}' was added with "
                    f"value: {standardizes_value(value['second'])}"
                )
            )
        elif status == ONLY_1:
            result.append(f"Property '{name}' was removed")
        elif status == NOT_EQUAL:
            result.append(
                (
                    f"Property '{name}' was updated. "
                    f"From {standardizes_value(value['first'])} "
                    f"to {standardizes_value(value['second'])}"
                )
            )
        elif status == NESTED:
            result.append(plain(node["chieldren"], name))
    return "\n".join(result)


def standardizes_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, (bool, int, type(None))):
        return dumps(value)
    else:
        return f"'{value}'"
