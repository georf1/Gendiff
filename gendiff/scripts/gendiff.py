#!/usr/bin/env python
from gendiff.get_diff_engine import get_diff
from gendiff.cli import display_cli
from gendiff.formatter import format_with_formatter


def generate_diff(first_file=None, second_file=None, formatter='stylish'):
    if first_file and second_file:
        diff = get_diff(first_file, second_file)
        result = format_with_formatter(formatter, diff)

        return result
    else:
        first_file, second_file, formatter = display_cli()
        diff = get_diff(first_file, second_file)
        result = format_with_formatter(formatter, diff)

        print(result)


def main():
    generate_diff()


if __name__ == '__main__':
    main()
