from json import dumps


SPACE = " "
INDENT = 4
SIGNED_INDENT = INDENT - 2
OPEN_BRACKET = "{"
CLOSING_BRACKET = "}"


def stylish(tree):
    formatted_tree_to_string = "{}\n{}\n{}"
    return formatted_tree_to_string.format(
        OPEN_BRACKET, analyzes_node(tree), CLOSING_BRACKET
    )


def analyzes_node(nodes, floor=1):
    result = []
    for node in nodes:
        status = node["status"]
        name = node["name"]
        value = node.get("value")
        node_type = node.get("node_type")
        if status == "nested":
            result.extend(
                [
                    f"{SPACE * INDENT * floor}{name}: {OPEN_BRACKET}",
                    analyzes_node(node["chieldren"], floor + 1),
                    f"{SPACE * INDENT * floor}{CLOSING_BRACKET}",
                ]
            )
        else:
            result.append(
                routes_analysis(name, value, status, floor, node_type)
            )
    return "\n".join(result)


def routes_analysis(name, value, status, floor, node_type="leaf"):
    result = []
    if status == "only_1":
        result.append(get_line(name, value["first"], "-", floor, node_type))
    elif status == "only_2":
        result.append(get_line(name, value["second"], "+", floor, node_type))
    elif status == "equal":
        result.append(get_line(name, value["first"], " ", floor, node_type))
    elif status == "not_equal":
        node_type1 = "dir" if isinstance(value["first"], dict) else "leaf"
        node_type2 = "dir" if isinstance(value["second"], dict) else "leaf"
        result.append(get_line(name, value["first"], "-", floor, node_type1))
        result.append(get_line(name, value["second"], "+", floor, node_type2))
    return "\n".join(result)


def get_line(name, value, mark, floor, node_type="leaf"):
    floors_list = []
    indent = SPACE * (INDENT * floor - SIGNED_INDENT)
    if node_type == "leaf":
        value = dumps(value) if isinstance(value, (bool, type(None))) else value
        if value == "":
            floors_list.append(f"{indent}{mark} {name}:")
        else:
            floors_list.append(f"{indent}{mark} {name}: {value}")
    else:
        floors_list.extend(
            [
                f"{indent}{mark} {name}: {OPEN_BRACKET}",
                expands_dir_node(value, floor + 1),
                f"{indent}  {CLOSING_BRACKET}",
            ]
        )
    return "\n".join(floors_list)


def expands_dir_node(value, floor):
    floors_list = []
    for key in value.keys():
        name = key
        val = value[key]
        mark = " "
        node_type = "dir" if isinstance(val, dict) else "leaf"
        floors_list.append(get_line(name, val, mark, floor, node_type))
    return "\n".join(floors_list)
