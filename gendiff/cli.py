import argparse


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', dest='extension', nargs='?',
                        default='stylish', type=str,
                        help='set format of output')

    return parser.parse_args()
