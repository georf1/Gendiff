import json
import yaml


def open_file(path_to_file):
    file_name, extension = path_to_file.split('.')
    with open(path_to_file) as file:
        return load_file(file, extension)


def load_file(file, extension):
    if extension.lower() == 'json':
        return json.load(file)
    elif extension.lower() == 'yaml' or 'yaml':
        return yaml.load(file, Loader=yaml.Loader)
