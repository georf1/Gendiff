from gendiff.get_diff_engine import get_diff


def to_str(value):
    if value in [True, False, None]:
        if value is None:
            return 'null'
        return str(value).lower()
    return value


def display_diff(diff):     # noqa: C901
    result = ['{\n']

    def walk(structure, depth):
        for data in structure:
            spaces = (2 + depth) * ' '
            status = '  '

            if data['status'] == 'removed':
                status = '- '
            elif data['status'] == 'added':
                status = '+ '

            if data['status'] == 'nested':
                result.append(f'{spaces}  {data["key"]}: {{\n')
                result.append(walk(data['children'], depth + 4))
                result.append(f'{spaces}  }}\n')

            elif isinstance(data['value'], dict):
                result.append(f'{spaces}{status}{data["key"]}: {{\n')
                result.append(walk(get_diff(data['value'], data['value']),
                              depth + 4))
                result.append(f'{spaces}  }}\n')

            elif data['status'] == 'changed':
                if isinstance(data['value'][0], dict):
                    inner_diff = get_diff(data['value'][0], data['value'][0])

                    result.append(f'{spaces}- {data["key"]}: {{\n')
                    result.append(walk(inner_diff, depth + 4))
                    result.append(f'{spaces}  }}\n')
                    result.append(f'{spaces}+ {data["key"]}: '
                                  f'{to_str(data["value"][1])}\n')
                elif isinstance(data['value'][1], dict):
                    inner_diff = get_diff(data['value'][1], data['value'][1])

                    result.append(f'{spaces}- {data["key"]}: '
                                  f'{to_str(data["value"][0])}\n')
                    result.append(f'{spaces}+ {data["key"]}: {{\n')
                    result.append(walk(inner_diff, depth + 4))
                    result.append(f'{spaces}  }}\n')
                else:
                    result.append(f'{spaces}- {data["key"]}: '
                                  f'{to_str(data["value"][0])}\n')
                    result.append(f'{spaces}+ {data["key"]}: '
                                  f'{to_str(data["value"][1])}\n')

            else:
                result.append(f'{spaces}{status}{data["key"]}: '
                              f'{to_str(data["value"])}\n')
        return ''

    walk(diff, 0)
    result.append('}')

    return ''.join(result)
