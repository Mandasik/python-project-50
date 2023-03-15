from json import load
from itertools import chain


def get_str_rec(file_one, file_two, key):
    if key in file_one and key in file_two:
        first, second = file_one[key], file_two[key]
        same = f"{key}: {first}"
        different = (f"- {key}: {first}", f"+ {key}: {second}")
        return same if first == second else different
    else:
        return (
            f"- {key}: {file_one[key]}"
            if key in file_one
            else f"+ {key}: {file_two[key]}"
        )


def get_dict_from_json(path):
    with open(path, "r") as fp:
        return load(fp)


def generate_diff(path1, path2):
    result = []
    file_one = get_dict_from_json(path1)
    file_two = get_dict_from_json(path2)
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
