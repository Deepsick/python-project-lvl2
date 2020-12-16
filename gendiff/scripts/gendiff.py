from gendiff import args_parser
from gendiff.comparator import generate_diff


def main():
    args = args_parser.parse()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
