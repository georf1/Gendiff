def transform(value):
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

    def walk(data, path=''):
        for inter_data in data:
            path += f".{inter_data['key']}" if path else f"{inter_data['key']}"

            if inter_data['status'] == 'nested':
                walk(inter_data['children'], path)
            elif inter_data['status'] == 'removed':
                result.append(f"Property '{path}' was removed")
            elif inter_data['status'] == 'added':
                result.append(f"Property '{path}' was added "
                              + f"with value: {transform(inter_data['value'])}")
            elif inter_data['status'] == 'changed':
                result.append(f"Property '{path}' was updated. "
                              + f"From {transform(inter_data['value'][0])} "
                              + f"to {transform(inter_data['value'][1])}")

            path = '.'.join(path.split('.')[:-1])
    walk(diff)
    return '\n'.join(result)
