import argparse
from gendiff.parser import pair_files_loader
from gendiff.diff import diff_mapping
from gendiff.formatters.stylish import stylish


def generate_diff(file1, file2, format=stylish):

    dict1, dict2 = pair_files_loader(file1, file2)
    mapping = diff_mapping(dict1, dict2)
    result = stylish(mapping)
    return result


def main():

    desc = 'Compares two configuration files and whows a difference.'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('file_1', metavar='first_file')
    parser.add_argument('file_2', metavar='second_file')

    args = parser.parse_args()
    result = generate_diff(args.file_1, args.file_2)
    print(result)


if __name__ == '__main__':
    main()
