from gendiff.formatters import stylish, plain, json

map_format_to_formatter = {
    "plain": plain.format,
    "stylish": stylish.format,
    "json": json.format
}


def format(tree, format):
    if format not in map_format_to_formatter:
        raise ValueError("This format isn't supported")

    return map_format_to_formatter[format](tree)
