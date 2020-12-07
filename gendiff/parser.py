import json
import yaml

map_format_to_parser = {
    'json': json.load,
    'yml': yaml.safe_load
}


def parse(content, format):
    if format not in map_format_to_parser:
        raise ValueError("This format isn't supported")

    return map_format_to_parser[format](content)
