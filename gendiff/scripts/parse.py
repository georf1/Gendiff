import json
import yaml


def get_file_format(file: str):
    if file.endswith('json'):
        return json.load(open(file))
    else:
        return yaml.load(open(file), Loader=yaml.Loader)


def get_diff(path_to_first_file: str, path_to_second_file: str):
    first_file = get_file_format(path_to_first_file)
    second_file = get_file_format(path_to_second_file)

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
