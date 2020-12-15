from gendiff.node_types import NODE_TYPE

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


def format(node, depth=0):
    node_type = node["type"]
    key = node.get("key")
    indent = make_indent(depth)
    children = node.get('children')

    if node_type == NODE_TYPE["origin"]:
        rows = [f'{indent}{format(child, depth)}\n' for child in children]
        return f'{{\n{"".join(rows)}}}'

    if node_type == NODE_TYPE["nested"]:
        rows = [f'{format(child, depth + 1)}\n' for child in children]
        result = "".join(rows)
        return (
            f'{indent}    {key}: {{\n{result}{make_indent(depth + 1)}}}'
        )

    if node_type == NODE_TYPE["added"]:
        return (
            f'{indent}  + {key}: {stringify(node["value"], depth)}'
        )

    if node_type == NODE_TYPE["removed"]:
        return (
            f'{indent}  - {key}: {stringify(node["value"], depth)}'
        )

    if node_type == NODE_TYPE["updated"]:
        return '\n'.join([
            f'{indent}  - {key}: {stringify(node["old_value"], depth)}',
            f'{indent}  + {key}: {stringify(node["new_value"], depth)}'
        ])

    if node_type == NODE_TYPE["unchanged"]:
        return (
            f'{indent}    {key}: {stringify(node["value"], depth)}'
        )

    raise ValueError('There is no such node type')
