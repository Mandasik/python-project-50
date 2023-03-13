#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(usage=(f'gendiff [-h] [-f FORMAT]' 
                                     f' first_file second_file'),
                                     description='Compares two \
                                        configuration files and \
                                            shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()
print(args)


def main():
    pass


if __name__ == '__main__':
    main()
