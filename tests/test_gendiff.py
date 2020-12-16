import pytest
import os
import pathlib
import json
from gendiff.comparator import generate_diff
from gendiff import parser
from gendiff.formatters import formatter

FIXTURES_DIR = 'fixtures'
formats = parser.FORMATS.keys()
output_formats = formatter.FORMATS.keys()


def get_path(file_name):
    dir_path = pathlib.Path(__file__).absolute().parent
    return os.path.join(dir_path, FIXTURES_DIR, file_name)


def read_file(path):
    with open(path) as f:
        result = f.read()
    return result


map_format_to_result = {}
for format in output_formats:
    map_format_to_result[format] = read_file(
        get_path(f'result.{format}')
    )


@pytest.mark.parametrize('format', formats)
def test_gendiff_format(format):
    """Check that format is working correctly."""
    file_path_1 = get_path(f'file1.{format}')
    file_path_2 = get_path(f'file2.{format}')
    for output_format in output_formats:
        diff = generate_diff(file_path_1, file_path_2, output_format)

        if output_format == formatter.FORMATS["json"]:
            json_result = map_format_to_result[output_format]
            assert json.loads(diff) == json.loads(json_result)
            continue
        assert diff == map_format_to_result[output_format]


def test_gendiff_default():
    """Check that stylish format is applied by default."""
    file_path_1 = get_path('file1.json')
    file_path_2 = get_path('file2.yml')
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == map_format_to_result['stylish']
