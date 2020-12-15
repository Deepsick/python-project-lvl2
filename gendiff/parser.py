import json
import yaml

parsers = {
    'json': json.load,
    'yml': yaml.safe_load
}


def parse(content, format):
    if format not in parsers:
        raise ValueError("This format isn't supported")

    return parsers[format](content)
