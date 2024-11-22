def iter(current_value, path):
    lines = []
    for i in current_value:
        if path and not path.endswith('.'):
            path += '.'
        match i.get('type'):
            case 'nested':
                lines.append(iter(i['value'], path=path + i['key']))
            case 'added':
                lines.append(f"Property '{path + i['key']}' "
                             f"was added with value: {make_string(i['value'])}")
            case 'removed':
                lines.append(f"Property '{path + i['key']}' was removed")
            case 'updated':
                lines.append(f"Property '{path + i['key']}' was updated. "
                             f"From {make_string(i['value1'])} "
                             f"to {make_string(i['value2'])}")
    return '\n'.join(lines)


def format(data):
    return iter(data, '')


def make_string(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{str(value)}'"
