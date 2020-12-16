from gendiff.tree import NODE_TYPES


def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, str):
        return f"'{value}'"

    if value is None:
        return "null"

    return str(value).lower()


def flat_list(items):
    flatten_rows = []

    if type(items) != list:
        return [items]
    for item in items:
        flatten_rows.extend(flat_list(item))

    return flatten_rows


def format(node):
    node_type = node["type"]
    key = node.get("key")
    children = node.get("children")

    if node_type == NODE_TYPES['origin']:
        rows = [format(child) for child in children]
        return '\n'.join(flat_list(rows))

    if node_type == NODE_TYPES["nested"]:
        rows = []
        for child in children:
            child["key"] = f'{key}.{child["key"]}'
            rows.append(format(child))
        return rows

    if node_type == NODE_TYPES["added"]:
        value = stringify(node['value'])
        return (
            f"Property '{key}' was added with value: {value}"
        )

    if node_type == NODE_TYPES["removed"]:
        return f"Property '{key}' was removed"

    if node_type == NODE_TYPES["updated"]:
        value = stringify(node['old_value'])
        new_value = stringify(node['new_value'])
        return (
            f"Property '{key}' was updated. From {value} to {new_value}"
        )

    if node_type == NODE_TYPES["unchanged"]:
        return []

    raise ValueError('There is no such node type')
