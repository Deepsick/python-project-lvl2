from gendiff.node_types import NODE_TYPE


def get_diff(first_object, second_object):
    union_keys = first_object.keys() | second_object.keys()
    tree = []
    for key in sorted(union_keys):
        if key not in first_object:
            tree.append({
                'type': NODE_TYPE["added"],
                'key': key,
                'value': second_object[key]
            })
            continue

        if key not in second_object:
            tree.append({
                'type': NODE_TYPE["removed"],
                'key': key,
                'value': first_object[key]
            })
            continue

        if isinstance(
            first_object[key],
            dict
        ) and isinstance(second_object[key], dict):
            tree.append({
                'type': NODE_TYPE["nested"],
                'key': key,
                'children': get_diff(first_object[key], second_object[key])
            })
            continue

        if first_object[key] != second_object[key]:
            tree.append({
                'type': NODE_TYPE["updated"],
                'key': key,
                'old_value': first_object[key],
                'new_value': second_object[key]
            })
            continue

        tree.append({
            'type': NODE_TYPE["unchanged"],
            'key': key,
            'value': first_object[key]
        })

    return tree


def build_diff(first_object, second_object):
    return {
        'type': NODE_TYPE["origin"],
        'children': get_diff(first_object, second_object)
    }
