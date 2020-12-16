from gendiff.tree import NODE_TYPES

INDENT_TYPE = " "
INDENT_SIZE = 4


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


def make_indent(depth, indent_size=INDENT_SIZE, indent_type=INDENT_TYPE):
    return indent_type * indent_size * depth


def format(node, depth=0):
    node_type = node["type"]
    key = node.get("key")
    indent = make_indent(depth)
    children = node.get('children')

    if node_type == NODE_TYPES["origin"]:
        rows = [f'{indent}{format(child, depth)}\n' for child in children]
        return f'{{\n{"".join(rows)}}}'

    if node_type == NODE_TYPES["nested"]:
        rows = [f'{format(child, depth + 1)}\n' for child in children]
        result = "".join(rows)
        return (
            f'{indent}    {key}: {{\n{result}{make_indent(depth + 1)}}}'
        )

    if node_type == NODE_TYPES["added"]:
        return (
            f'{indent}  + {key}: {stringify(node["value"], depth)}'
        )

    if node_type == NODE_TYPES["removed"]:
        return (
            f'{indent}  - {key}: {stringify(node["value"], depth)}'
        )

    if node_type == NODE_TYPES["updated"]:
        return '\n'.join([
            f'{indent}  - {key}: {stringify(node["old_value"], depth)}',
            f'{indent}  + {key}: {stringify(node["new_value"], depth)}'
        ])

    if node_type == NODE_TYPES["unchanged"]:
        return (
            f'{indent}    {key}: {stringify(node["value"], depth)}'
        )

    raise ValueError('There is no such node type')
