import json
import yaml

FORMATS = {
    "json": "json",
    "yml": "yml",
    "yaml": "yaml"
}


def parse(content, format):
    if format == FORMATS["json"]:
        return json.load(content)

    if format == FORMATS["yml"] or format == FORMATS["yaml"]:
        return yaml.safe_load(content)

    raise ValueError(
        f'''{format} format isn't supported.
        Supported formats: {', '.join(FORMATS.keys())}'''
    )
