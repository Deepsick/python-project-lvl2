from gendiff.const import KeyType


def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, str):
        return f"'{value}'"

    if value is None:
        return "null"

    return str(value).lower()


def format(nodes):
    result = []
    for node in nodes:
        node_type = node["type"]
        key = node["key"]

        if node_type == KeyType["NESTED"]:
            children = node["children"][:]
            for child in children:
                child["key"] = f'{key}.{child["key"]}'
            result.append(format(children))

        if node_type == KeyType["ADDED"]:
            value = stringify(node['value'])
            result.append(
                f"Property '{key}' was added with value: {value}"
            )

        if node_type == KeyType["REMOVED"]:
            result.append(f"Property '{key}' was removed")

        if node_type == KeyType["UPDATED"]:
            value = stringify(node['old_value'])
            new_value = stringify(node['new_value'])
            result.append(
                f"Property '{key}' was updated. From {value} to {new_value}"
            )

    return '\n'.join(result)
