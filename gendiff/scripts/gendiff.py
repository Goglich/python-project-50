import argparse
from gendiff.module import gendiff
from ..parser import files_parser
from ..formater import formater


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    data1, data2 = files_parser(args.first_file, args.second_file)
    print(formater.make_stylish(gendiff.generate_diff(data1, data2)))


if __name__ == "__main__":
    main()
