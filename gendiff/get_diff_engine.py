def get_diff(structure1, structure2):      # noqa: C901
    diff = []

    for key in sorted(structure1 | structure2):
        if key not in structure2:
            diff.append({'key': key,
                         'value': structure1[key],
                         'status': 'removed'})
        elif key not in structure1:
            diff.append({'key': key,
                         'value': structure2[key],
                         'status': 'added'})
        elif isinstance(structure1[key], dict) \
                and isinstance(structure2[key], dict):
            children = get_diff(structure1[key], structure2[key])
            diff.append({'key': key,
                         'status': 'nested',
                         'children': children})
        elif structure1[key] != structure2[key]:
            diff.append({'key': key,
                         'value': [structure1[key], structure2[key]],
                         'status': 'changed'})
        elif structure2[key] == structure1[key]:
            diff.append({'key': key,
                         'value': structure2[key],
                         'status': 'unchanged'})

    return diff
