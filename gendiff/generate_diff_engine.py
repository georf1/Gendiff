from gendiff.get_diff_engine import get_diff
from gendiff.formatter import format_with_formatter
from gendiff.parse import open_file


def generate_diff(first_file, second_file, formatter='stylish'):
    first_file = open_file(first_file)
    second_file = open_file(second_file)

    diff = get_diff(first_file, second_file)
    result = format_with_formatter(formatter, diff)

    return result
