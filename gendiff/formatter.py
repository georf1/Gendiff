from gendiff.formatters.stylish import display_diff as display_diff_stylish


def format_with_formatter(formatter, diff):
    if formatter == 'stylish':
        return display_diff_stylish(diff)
