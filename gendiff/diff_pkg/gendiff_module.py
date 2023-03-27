from os.path import splitext
from itertools import chain
import json
import yaml
from yaml.loader import SafeLoader


def generate_diff(path1: str, path2: str, format='stylish'):
    tree_diff = get_tree(get_dict(path1), get_dict(path2))
    return tree_diff


def get_format(path):
    _, extension = splitext(path)
    return extension.lower()


def get_dict(path):
    if get_format(path) == '.json':
        with open(path, "r") as fp:
            return json.load(fp)
    else:
        try:
            with open(path, "r") as fp:
                return yaml.load(fp, Loader=SafeLoader)
        except: # NOQA E722
            print('This format is not supported')
            return 'not supported'


def get_tree(d_first: dict, d_second: dict):
    tree = []
    all_keys = chain(
        d_first.keys(),
        [x for x in d_second.keys() if x not in d_first.keys()]
    )
    for key in sorted(all_keys):
        description = type_of_leaf(d_first, d_second, key)
        if description != 'dir':
            values = value_of_leaf(d_first, d_second, key, description)
            tree.append(get_node(key, description, value=values))
        else:
            chieldren = get_tree(d_first[key], d_second[key])
            tree.append(get_node(key, description, chieldren=chieldren))
    return tree


def type_of_leaf(d_first: dict, d_second: dict, key: str):
    inters = set(d_first.keys()) & set(d_second.keys())
    only_first = set(d_first.keys()) - set(d_second.keys())
    if key in sorted(inters):
        if isinstance(d_first[key], dict) and isinstance(d_second[key], dict):
            return 'dir'
        return 'equal' if d_first[key] == d_second[key] else 'not equal'
    else:
        return 'only 1' if key in only_first else 'only 2'


def value_of_leaf(d_first, d_second, key, description):
    if description == 'equal' or description == 'only 1':
        return {'first': d_first[key]}
    elif description == 'not equal':
        return {'first': d_first[key], 'second': d_second[key]}
    else:
        return {'second': d_second[key]}


def get_node(name: str, type_leaf: str, value=None, chieldren=None):
    if type_leaf == 'dir':
        return {'name': name, 'node type': type_leaf, 'chieldren': chieldren}
    else:
        return {'name': name, 'node type': type_leaf, 'value': value}
