from gendiff.formatters.stylish import display_diff as display_diff_stylish
from gendiff.formatters.plain import display_diff as display_diff_plain


def format_with_formatter(formatter, diff):
    if formatter == 'stylish':
        return display_diff_stylish(diff)
    elif formatter == 'plain':
        return display_diff_plain(diff)
