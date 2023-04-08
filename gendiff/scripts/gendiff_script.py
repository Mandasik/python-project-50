#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        usage="gendiff [-h] [-f FORMAT] \
                                 first_file second_file",
        description="Compares two configuration \
                                    files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output",
                        default="stylish")

    args = parser.parse_args()
    print(args)
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
