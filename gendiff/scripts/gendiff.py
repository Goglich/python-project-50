from gendiff.generate_diff import generate_diff
from gendiff import cli


def main():
    print(generate_diff(cli.first_file, cli.second_file, cli.format))


if __name__ == "__main__":
    main()
