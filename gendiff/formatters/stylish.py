from gendiff.get_diff_engine import get_diff


def to_str(value):
    if value in [True, False, None]:
        if value is None:
            return 'null'
        return str(value).lower()
    return value


def display_diff(diff):     # noqa: C901
    result = ['{\n']

    def walk(data, depth):
        for x in data:
            spaces = (2 + depth) * ' '
            status = '  '

            if x['status'] == 'removed':
                status = '- '
            elif x['status'] == 'added':
                status = '+ '

            if x['status'] == 'nested':
                result.append(spaces + '  ' + f'{x["key"]}: ' + '{\n')
                result.append(walk(x['children'], depth + 4))
                result.append(spaces + '  ' + '}\n')

            elif isinstance(x['value'], dict):
                result.append(spaces + status + f'{x["key"]}: ' + '{\n')
                result.append(walk(get_diff(x['value'], x['value']), depth + 4))
                result.append(spaces + '  ' + '}\n')

            elif x['status'] == 'changed':
                if isinstance(x['value'][0], dict):
                    inter_diff = get_diff(x['value'][0], x['value'][0])

                    result.append(spaces + '- ' + f'{x["key"]}: ' + '{\n')
                    result.append(walk(inter_diff, depth + 4))
                    result.append(spaces + '  ' + '}\n')
                    result.append(spaces + '+ '
                                  + f'{x["key"]}: {to_str(x["value"][1])}\n')
                elif isinstance(x['value'][1], dict):
                    inter_diff = get_diff(x['value'][1], x['value'][1])

                    result.append(spaces + '- '
                                  + f'{x["key"]}: {to_str(x["value"][0])}\n')
                    result.append(spaces + '+ ' + f'{x["key"]}: ' + '{\n')
                    result.append(walk(inter_diff, depth + 4))
                    result.append(spaces + '  ' + '}\n')
                else:
                    result.append(spaces + '- '
                                  + f'{x["key"]}: {to_str(x["value"][0])}\n')
                    result.append(spaces + '+ '
                                  + f'{x["key"]}: {to_str(x["value"][1])}\n')

            else:
                result.append(spaces + status
                              + f'{x["key"]}: {to_str(x["value"])}\n')

        return ''

    walk(diff, 0)
    result.append('}')

    return ''.join(result)
