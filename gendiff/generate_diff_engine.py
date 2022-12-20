from gendiff.get_diff_engine import get_diff
from gendiff.formatter import format_with_formatter


def generate_diff(first_file, second_file, formatter='stylish'):
    diff = get_diff(first_file, second_file)
    result = format_with_formatter(formatter, diff)

    return result
