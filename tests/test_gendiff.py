import pytest
import os
from gendiff.comparator import generate_diff
import pathlib

FIXTURES_DIR = 'fixtures'
FORMATS = ['json', 'yml']
OUTPUT_FORMATS = ['plain', 'stylish', 'json']


def get_path(file_name):
    dir_path = pathlib.Path(__file__).absolute().parent
    return os.path.join(dir_path, FIXTURES_DIR, file_name)


def read_file(path):
    with open(path) as f:
        result = f.read()
    return result


map_format_to_result = {}
for format in OUTPUT_FORMATS:
    map_format_to_result[format] = read_file(
        get_path(f'result.{format}')
    )


@pytest.mark.parametrize('format', FORMATS)
def test_gendiff_format(format):
    """Check that format is working correctly."""
    file_path_1 = get_path(f'file1.{format}')
    file_path_2 = get_path(f'file2.{format}')
    for format in OUTPUT_FORMATS:
        diff = generate_diff(file_path_1, file_path_2, format)
        assert diff == map_format_to_result[format]


def test_gendiff_default():
    """Check that stylish format is applied by default."""
    file_path_1 = get_path('file1.json')
    file_path_2 = get_path('file2.yml')
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == map_format_to_result['stylish']
