#!/usr/bin/env python
from gendiff.cli import parse_args
from gendiff.generate_diff_engine import generate_diff


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file,
                        args.extension))


if __name__ == '__main__':
    main()
