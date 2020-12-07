from os.path import abspath, splitext
from gendiff import parser, tree_builder
from gendiff.formatters import formatter


def get_file_format(file_path):
    _, file_extension = splitext(file_path)
    return file_extension[1:]


def generate_diff(file_path_1, file_path_2, format="stylish"):
    data_1 = open(abspath(file_path_1))
    data_2 = open(abspath(file_path_2))

    parsed_data_1 = parser.parse(data_1, get_file_format(file_path_1))
    parsed_data_2 = parser.parse(data_2, get_file_format(file_path_2))

    diff_tree = tree_builder.build_diff(parsed_data_1, parsed_data_2)
    return formatter.format(diff_tree, format)
