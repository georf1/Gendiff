from gendiff.get_diff_engine import get_diff


def display_diff(diff):     # noqa: C901
    result = ['{\n', '}']

    def walk(data, depth):
        for x in data:
            spaces_count = 2 + depth

            if x['status'] == 'removed':
                status = '- '
            elif x['status'] == 'added':
                status = '+ '
            elif x['status'] == 'changed':
                status = '- + '
            else:
                status = '  '

            if x['status'] == 'nested':
                result.insert(-1, ' ' * (spaces_count + 2) + f'{x["key"]}: '
                              + '{\n')
                result.insert(-1, walk(x['children'], depth + 4))
                result.insert(-1, ' ' * (spaces_count + 2) + '}\n')
            elif isinstance(x['value'], dict):
                x['value'] = get_diff(x['value'], x['value'])
                result.insert(-1, ' ' * spaces_count + status + f'{x["key"]}: '
                              + '{\n')
                result.insert(-1, walk(x['value'], depth + 4))
                result.insert(-1, ' ' * (spaces_count + 2) + '}\n')
            elif x['status'] == 'changed':
                if isinstance(x['value'][0], dict):
                    x['value'][0] = get_diff(x['value'][0], x['value'][0])
                    result.insert(-1, ' ' * spaces_count + status[0:2]
                                  + f'{x["key"]}: ' + '{\n')
                    result.insert(-1, walk(x['value'][0], depth + 4))
                    result.insert(-1, ' ' * (spaces_count + 2) + '}\n')
                    result.insert(-1, ' ' * spaces_count + status[2:]
                                  + f'{x["key"]}: {x["value"][1]}\n')
                elif isinstance(x['value'][1], dict):
                    x['value'][1] = get_diff(x['value'][1], x['value'][1])
                    result.insert(-1, ' ' * spaces_count + status[0:2]
                                  + f'{x["key"]}: {x["value"][0]}\n')
                    result.insert(-1, ' ' * spaces_count + status[2:]
                                  + f'{x["key"]}: ' + '{\n')
                    result.insert(-1, walk(x['value'][1], depth + 4))
                    result.insert(-1, ' ' * (spaces_count + 2) + '}\n')
                else:
                    result.insert(-1, ' ' * spaces_count + status[0:2]
                                  + f'{x["key"]}: {x["value"][0]}\n')
                    result.insert(-1, ' ' * spaces_count + status[2:]
                                  + f'{x["key"]}: {x["value"][1]}\n')
            else:
                result.insert(-1, ' ' * spaces_count + status
                              + f'{x["key"]}: {x["value"]}\n')

        return ''

    walk(diff, 0)
    return ''.join(result)
