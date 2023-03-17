from os.path import splitext
import json
import yaml
from yaml.loader import SafeLoader
from itertools import chain


def get_str_rec(file_one, file_two, key):
    if key in file_one and key in file_two and file_one[key] == file_two[key]:
        return f"{key}: {file_one[key]}"
    elif key in file_one and key in file_two and file_one[key] != file_two[key]:
        different = (f"- {key}: {file_one[key]}", f"+ {key}: {file_two[key]}")
        return different
    else:
        return (
            f"- {key}: {file_one[key]}"
            if key in file_one
            else f"+ {key}: {file_two[key]}"
        )


def get_dict(path):
    _, extension = splitext(path)
    if extension == '.json':
        with open(path, "r") as fp:
            return json.load(fp)
    else:
        with open(path, "r") as fp:
            return yaml.load(fp, Loader=SafeLoader)


def generate_diff(path1, path2):
    result = []
    file_one = get_dict(path1)
    file_two = get_dict(path2)
    all_keys = chain(
        file_one.keys(),
        [x for x in file_two.keys() if x not in file_one.keys()]
    )
    for key in sorted(all_keys):
        compare = get_str_rec(file_one, file_two, key)
        if isinstance(compare, tuple):
            first, second = compare
            result.append(first)
            result.append(second)
        else:
            result.append(compare)
    return "\n".join(result)
