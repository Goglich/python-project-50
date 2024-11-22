from gendiff.generate_diff import generate_diff
from gendiff import cli


def main():
    first_file, second_file, format = cli.parse_args()
    print(generate_diff(first_file, second_file, format))


if __name__ == "__main__":
    main()
