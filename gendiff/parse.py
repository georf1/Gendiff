import json
import yaml


def open_file(file):
    if file.endswith('json'):
        return json.load(open(file))
    else:
        return yaml.load(open(file), Loader=yaml.Loader)
