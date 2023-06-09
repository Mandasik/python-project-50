from os.path import splitext
from itertools import chain
import json
import yaml
from yaml.loader import SafeLoader
from gendiff.format_pkg import stylish_format
from gendiff.format_pkg import plain_format
from gendiff.format_pkg import json_format
from gendiff.format_pkg.constans import (
    ONLY_1, ONLY_2, EQUAL, NOT_EQUAL, NESTED
)


def generate_diff(path1: str, path2: str, format_out="stylish"):
    tree_diff = get_tree(get_dict(path1), get_dict(path2))
    if format_out == "stylish":
        tree_out = stylish_format.stylish(tree_diff)
    elif format_out == "plain":
        tree_out = plain_format.plain(tree_diff)
    elif format_out == "json":
        tree_out = json_format.json_f(tree_diff)
    else:
        return "This format is not supported"
    return tree_out


def get_format(path):
    _, extension = splitext(path)
    return extension.lower()


def get_dict(path):
    if get_format(path) == ".json":
        with open(path, "r") as fp:
            return json.load(fp)
    else:
        try:
            with open(path, "r") as fp:
                return yaml.load(fp, Loader=SafeLoader)
        except:  # NOQA E722
            print("This format is not supported")
            return "not supported"


def get_tree(d_first: dict, d_second: dict):
    tree = []
    all_keys = chain(
        d_first.keys(), [x for x in d_second.keys() if x not in d_first.keys()]
    )
    for key in sorted(all_keys):
        description = status_of_node(d_first, d_second, key)
        if description != NESTED:
            values = value_of_leaf(d_first, d_second, key, description)
            type_node = type_of_node(d_first, d_second, key)
            tree.append(get_node(key, description, type_node, value=values))
        else:
            chieldren = get_tree(d_first[key], d_second[key])
            tree.append(get_node(key, description, chieldren=chieldren))
    return tree


def type_of_node(d_fir: dict, d_second: dict, key: str):
    if isinstance(d_fir.get(key), dict) or isinstance(d_second.get(key), dict):
        return "dir"
    return "leaf"


def status_of_node(d_first: dict, d_second: dict, key: str):
    inters = set(d_first.keys()) & set(d_second.keys())
    only_first = set(d_first.keys()) - set(d_second.keys())
    if key in sorted(inters):
        if isinstance(d_first[key], dict) and isinstance(d_second[key], dict):
            return NESTED
        return EQUAL if d_first[key] == d_second[key] else NOT_EQUAL
    else:
        return ONLY_1 if key in only_first else ONLY_2


def value_of_leaf(d_first, d_second, key, description):
    if description == EQUAL or description == ONLY_1:
        return {"first": d_first[key]}
    elif description == NOT_EQUAL:
        return {"first": d_first[key], "second": d_second[key]}
    else:
        return {"second": d_second[key]}


def get_node(name, status, type_node=None, value=None, chieldren=None):
    if status == NESTED:
        return {
            "name": name,
            "status": status,
            "chieldren": chieldren,
        }
    else:
        return {
            "name": name,
            "node_type": type_node,
            "status": status,
            "value": value
        }
