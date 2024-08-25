import argparse
from gendiff.module import gendiff

def main():
    parser = argparse.ArgumentParser(
                        prog='gendiff',
                        description='Compares two configuration files and shows a difference.',
                        )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    # args = parser.parse_args()
    
    gendiff.generate_diff('module\file1.json', 'module\file2.json')

if __name__ == "__main__":
    main()