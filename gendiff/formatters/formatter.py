from gendiff.formatters import stylish, plain, json

formatters = {
    "plain": plain.format,
    "stylish": stylish.format,
    "json": json.format
}


def format(tree, format):
    if format not in formatters:
        raise ValueError("This format isn't supported")

    return formatters[format](tree)
