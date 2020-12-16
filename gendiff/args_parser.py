import argparse


def parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='stylish'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()
