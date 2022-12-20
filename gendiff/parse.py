import json
import yaml


def open_file(path_to_file):
    file_name, format_ = path_to_file.split('.')
    with open(path_to_file) as file:
        return load_file(file, format_)


def load_file(file, format_):
    if format_ == 'json':
        return json.load(file)
    elif format_ == 'yaml' or 'yaml':
        return yaml.load(file, Loader=yaml.Loader)
