#!/usr/bin/env python
import argparse
import json


DESCRIPTION = 'Compares two configuration files and shows a difference.'


def discern_diff(path_to_first_file: str, path_to_second_file: str):
    first_file = json.load(open(path_to_first_file))
    second_file = json.load(open(path_to_second_file))
    diff = {'removed': {},
            'added': {},
            'changed': {},
            'stayed': {}
            }

    for key in sorted(first_file | second_file):
        if first_file.get(key) is not None and second_file.get(key) is None:
            diff['removed'].update({key: first_file[key]})
        elif second_file.get(key) is not None and first_file.get(key) is None:
            diff['added'].update({key: second_file[key]})
        elif first_file.get(key) != second_file.get(key):
            diff['changed'].update({key: [first_file[key], second_file[key]]})
        elif second_file.get(key) is not None \
                and second_file.get(key) == first_file.get(key):
            diff['stayed'].update({key: second_file[key]})

    return diff


def display_diff(diff: dict):
    mapping = '{\n'
    keys = diff['removed'] | diff['added'] | diff['stayed'] | diff['changed']

    for key in sorted(keys):
        if key in diff['removed']:
            mapping += f'  - {key}: {diff["removed"][key]}\n'
        elif key in diff['added']:
            mapping += f'  + {key}: {diff["added"][key]}\n'
        elif key in diff['changed']:
            mapping += f'  - {key}: {diff["changed"][key][0]}\n'
            mapping += f'  + {key}: {diff["changed"][key][1]}\n'
        elif key in diff['stayed']:
            mapping += f'    {key}: {diff["stayed"][key]}\n'

    mapping += '}'

    return mapping.strip()


def generate_diff(first_file=None, second_file=None):
    if first_file and second_file:
        diff = discern_diff(first_file, second_file)
        mapping = display_diff(diff)

        return mapping
    else:
        parser = argparse.ArgumentParser(description=DESCRIPTION)
        parser.add_argument('first_file', metavar='first_file', type=str)
        parser.add_argument('second_file', metavar='second_file', type=str)
        parser.add_argument('-f', '--format', dest='FORMAT',
                            action='store', help='set format of output')

        args = parser.parse_args()
        diff = discern_diff(args.first_file, args.second_file)

        mapping = display_diff(diff)

        print(mapping)


def main():
    generate_diff()


if __name__ == '__main__':
    main()
