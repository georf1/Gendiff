import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def display_cli():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', dest='FORMAT', nargs='?',
                        default='stylish', type=str,
                        help='set format of output')

    args = parser.parse_args()
    return args.first_file, args.second_file, args.FORMAT
