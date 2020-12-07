import pytest
from gendiff.comparator import generate_diff


FORMATS = ['json', 'yml']
OUTPUT_FORMATS = ['plain', 'stylish', 'json']


def read_file(path):
    with open(path) as f:
        result = f.read()
    return result


map_format_to_result = {}
for format in OUTPUT_FORMATS:
    map_format_to_result[format] = read_file(
        f'./tests/fixtures/result.{format}')


@pytest.mark.parametrize('format', FORMATS)
def test_gendiff_format(format):
    """Check that format is working correctly."""
    file_path_1 = f'./tests/fixtures/file1.{format}'
    file_path_2 = f'./tests/fixtures/file2.{format}'
    for format in OUTPUT_FORMATS:
        diff = generate_diff(file_path_1, file_path_2, format)
        assert diff == map_format_to_result[format]


def test_gendiff_default():
    """Check that stylish format is applied by default."""
    file_path_1 = './tests/fixtures/file1.json'
    file_path_2 = './tests/fixtures/file2.yml'
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == map_format_to_result['stylish']
