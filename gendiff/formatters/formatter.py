from gendiff.formatters import stylish, plain, json

FORMATS = {
    "plain": "plain",
    "stylish": "stylish",
    "json": "json"
}


def format(tree, format):
    if format == FORMATS["plain"]:
        return plain.format(tree)

    if format == FORMATS["stylish"]:
        return stylish.format(tree)

    if format == FORMATS["json"]:
        return json.format(tree)

    raise ValueError(
        f'''{format} format isn't supported.
        Supported formats: {', '.join(FORMATS.keys())}'''
    )
