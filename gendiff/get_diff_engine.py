from gendiff.parse import open_file


def convert_bool(value):
    lower_bool = {True: 'true', False: 'false', None: 'null'}
    return lower_bool[value] \
        if isinstance(value, bool) or isinstance(value, type(None)) else value


def get_diff(first_object, second_object):      # noqa: C901
    if isinstance(first_object, dict) and isinstance(second_object, dict):
        pass
    else:
        first_object = open_file(first_object)
        second_object = open_file(second_object)

    def walk(structure1, structure2):
        diff = []
        for key in sorted(structure1 | structure2):
            structure1_lower_bool = convert_bool(structure1.get(key))
            structure2_lower_bool = convert_bool(structure2.get(key))

            if isinstance(structure1.get(key), dict) \
                    and isinstance(structure2.get(key), dict):
                children = walk(structure1.get(key), structure2.get(key))
                diff.append({'key': key, 'status': 'nested',
                             'children': children})
            elif key in structure1 and key not in structure2:
                diff.append({'key': key, 'value': structure1_lower_bool,
                             'status': 'removed'})
            elif key in structure2 and key not in structure1:
                diff.append({'key': key, 'value': structure2_lower_bool,
                             'status': 'added'})
            elif structure1.get(key) != structure2.get(key):
                diff.append({'key': key, 'value': [structure1_lower_bool,
                             structure2_lower_bool], 'status': 'changed'})
            elif key in structure2 \
                    and structure2.get(key) == structure1.get(key):
                diff.append({'key': key, 'value': structure2_lower_bool,
                             'status': 'stayed'})

        return diff
    return walk(first_object, second_object)
