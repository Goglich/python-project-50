def build_plain(data):

    def iter_(current_value, path):
        lines = []
        for i in current_value:
            if path and not path.endswith('.'):
                path += '.'
            if i.get('type') == 'nested':
                lines.append(iter_(i['value'], path=path + i['key']))
            elif i.get('type') == 'added':
                lines.append(f"Property '{path + i['key']}' was added with value: {to_str(i['value'])}")
            elif i.get('type') == 'removed':
                lines.append(f"Property '{path + i['key']}' was removed")
            elif i.get('type') == 'updated':
                lines.append(f"Property '{path + i['key']}' was updated. From {to_str(i['value1'])} to {to_str(i['value2'])}")
        return '\n'.join(lines)
    return iter_(data, '')


def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{str(value)}'"
