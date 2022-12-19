def transform(value):
    if value in ['true', 'false', 'null'] or isinstance(value, int):
        return value
    return f"'{value}'"


def display_diff(diff):     # noqa: C901
    result = []

    def walk(data, path=''):
        for x in data:
            path += f".{x['key']}" if path else f"{x['key']}"

            if isinstance(x.get('value'), dict):
                x['value'] = '[complex value]'
            elif isinstance(x.get('value'), str):
                x['value'] = transform(x['value'])

            if x['status'] == 'nested':
                walk(x['children'], path)
            elif x['status'] == 'removed':
                result.append(f"Property '{path}' was removed")
            elif x['status'] == 'added':
                result.append(f"Property '{path}' was added "
                              + f"with value: {x['value']}")
            elif x['status'] == 'changed':
                x['value'][0] = '[complex value]' \
                    if isinstance(x.get('value')[0], dict) \
                    else transform(x['value'][0])
                x['value'][1] = '[complex value]' \
                    if isinstance(x.get('value')[1], dict) \
                    else transform(x['value'][1])

                result.append(f"Property '{path}' was updated. "
                              + f"From {x['value'][0]} to {x['value'][1]}")
            path = '.'.join(path.split('.')[:-1])
    walk(diff)
    return '\n'.join(result)
