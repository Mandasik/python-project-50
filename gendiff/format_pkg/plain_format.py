from json import dumps


def plain(tree, path=""):
    result = []
    for node in tree:
        status = node["status"]
        name = node["name"]
        name = path + "." + node["name"] if path else node["name"]
        value = node.get("value")
        if status == "only_2":
            result.append(
                (
                    f"Property '{name}' was added with "
                    f"value: {standardizes_value(value['second'])}"
                )
            )
        elif status == "only_1":
            result.append(f"Property '{name}' was removed")
        elif status == "not_equal":
            result.append(
                (
                    f"Property '{name}' was updated. "
                    f"From {standardizes_value(value['first'])} "
                    f"to {standardizes_value(value['second'])}"
                )
            )
        elif status == "nested":
            result.append(plain(node["chieldren"], name))
    return "\n".join(result)


def standardizes_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, (bool, int, type(None))):
        return dumps(value)
    else:
        return f"'{value}'"
