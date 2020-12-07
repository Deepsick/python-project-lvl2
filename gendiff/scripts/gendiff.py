import argparse
from gendiff.comparator import generate_diff


def parse_args():
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


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
