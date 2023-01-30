import argparse
from gendiff.engine.generate_diff import generate_diff


def main():

    desc = 'Compares two configuration files and whows a difference.'
    parser = argparse.ArgumentParser(description=desc)
    h = 'set format of output'
    parser.add_argument('-f', '--format', help=h, default='stylish')
    parser.add_argument('file_1', metavar='first_file')
    parser.add_argument('file_2', metavar='second_file')

    args = parser.parse_args()
    print(generate_diff(args.file_1, args.file_2, args.format))


if __name__ == '__main__':
    main()
