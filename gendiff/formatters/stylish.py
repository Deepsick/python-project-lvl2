from gendiff.const import KeyType

DEFAULT_INDENT = "    "


def stringify(value, depth):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        result = []
        indent = make_indent(depth + 1)
        for key, value in value.items():
            str_value = stringify(value, depth + 1)
            result.append(
                f'{indent}    {key}: {str_value}\n')
        return f'{{\n{"".join(result)}{indent}}}'

    return value


def make_indent(depth, indent_type=DEFAULT_INDENT):
    return indent_type * depth


def format(nodes, depth=0):
    result = []
    for node in nodes:
        node_type = node["type"]
        if node_type == KeyType["NESTED"]:
            result.append(
                f'    {node["key"]}: {format(node["children"], depth + 1)}')

        if node_type == KeyType["ADDED"]:
            result.append(
                f'  + {node["key"]}: {stringify(node["value"], depth)}')

        if node_type == KeyType["REMOVED"]:
            result.append(
                f'  - {node["key"]}: {stringify(node["value"], depth)}')

        if node_type == KeyType["UPDATED"]:
            result.append(
                f'  - {node["key"]}: {stringify(node["old_value"], depth)}')
            result.append(
                f'  + {node["key"]}: {stringify(node["new_value"], depth)}')

        if node_type == KeyType["UNCHANGED"]:
            result.append(
                f'    {node["key"]}: {stringify(node["value"], depth)}')

    formatted_nodes = "".join(
        [f'{make_indent(depth)}{node}\n' for node in result])
    return f'{{\n{formatted_nodes}{make_indent(depth)}}}'
