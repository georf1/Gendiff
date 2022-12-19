from gendiff.formatters.stylish import display_diff as display_diff_stylish
from gendiff.formatters.plain import display_diff as display_diff_plain
from gendiff.formatters.to_json import display_diff as display_diff_json


def format_with_formatter(formatter, diff):
    if formatter == 'stylish':
        return display_diff_stylish(diff)
    elif formatter == 'plain':
        return display_diff_plain(diff)
    elif formatter == 'json':
        return display_diff_json(diff)
