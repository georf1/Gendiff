def get_diff(first_object, second_object):      # noqa: C901
    def walk(structure1, structure2):
        diff = []

        for key in sorted(structure1 | structure2):
            if key in structure1 and key not in structure2:
                diff.append({'key': key,
                             'value': structure1[key],
                             'status': 'removed'})
            elif key in structure2 and key not in structure1:
                diff.append({'key': key,
                             'value': structure2[key],
                             'status': 'added'})
            elif isinstance(structure1.get(key), dict) \
                    and isinstance(structure2.get(key), dict):
                children = walk(structure1[key], structure2[key])
                diff.append({'key': key,
                             'status': 'nested',
                             'children': children})
            elif structure1.get(key) != structure2.get(key):
                diff.append({'key': key,
                             'value': [structure1[key], structure2[key]],
                             'status': 'changed'})
            elif key in structure2 \
                    and structure2.get(key) == structure1.get(key):
                diff.append({'key': key,
                             'value': structure2[key],
                             'status': 'unchanged'})

        return diff
    return walk(first_object, second_object)
