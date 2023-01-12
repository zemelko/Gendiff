import argparse


def main():

  parser = argparse.ArgumentParser(description='Compares two   configuration files and whows a difference.')

  parser.add_argument('-f', '--format', help='set format of output')
  parser.add_argument('file_1', metavar='first_file')
  parser.add_argument('file_2', metavar='second_file')

  args = parser.parse_args()

  # result = gendiff(args.file_1, args.file_2)


if __name__ == '__main__':
  main()