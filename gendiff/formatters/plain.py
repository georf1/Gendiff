def to_str(value):
    if value in [True, False, None]:
        if value is None:
            return 'null'
        return str(value).lower()

    if isinstance(value, int):
        return value

    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def display_diff(diff):     # noqa: C901
    result = []

    def walk(structure, path=''):
        for data in structure:
            path += f".{data['key']}" if path else f"{data['key']}"

            if data['status'] == 'nested':
                walk(data['children'], path)
            elif data['status'] == 'removed':
                result.append(f"Property '{path}' was removed")
            elif data['status'] == 'added':
                result.append(f"Property '{path}' was added "
                              f"with value: {to_str(data['value'])}")
            elif data['status'] == 'changed':
                result.append(f"Property '{path}' was updated. "
                              f"From {to_str(data['value'][0])} "
                              f"to {to_str(data['value'][1])}")

            path = '.'.join(path.split('.')[:-1])
    walk(diff)
    return '\n'.join(result)
