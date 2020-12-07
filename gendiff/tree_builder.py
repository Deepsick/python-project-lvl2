from gendiff.const import KeyType


def get_diff(first_object, second_object):
    union_keys = first_object.keys() | second_object.keys()
    tree = []
    for key in sorted(union_keys):
        if key not in first_object:
            tree.append({
                'type': KeyType["ADDED"],
                'key': key,
                'value': second_object[key]
            })
            continue

        if key not in second_object:
            tree.append({
                'type': KeyType["REMOVED"],
                'key': key,
                'value': first_object[key]
            })
            continue

        if isinstance(
            first_object[key],
            dict
        ) and isinstance(second_object[key], dict):
            tree.append({
                'type': KeyType["NESTED"],
                'key': key,
                'children': get_diff(first_object[key], second_object[key])
            })
            continue

        if first_object[key] != second_object[key]:
            tree.append({
                'type': KeyType["UPDATED"],
                'key': key,
                'old_value': first_object[key],
                'new_value': second_object[key]
            })
            continue

        tree.append({
            'type': KeyType["UNCHANGED"],
            'key': key,
            'value': first_object[key]
        })

    return tree


def build_diff(first_object, second_object):
    return {
        'type': 'origin',
        'children': get_diff(first_object, second_object)
    }
