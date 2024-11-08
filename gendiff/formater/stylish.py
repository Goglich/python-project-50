import itertools


INDENT = 4
SHIFT_LEFT = 2
STEP = 1


def make_stylish(value, replacer=' ', spaces_count=4):
    def iter_(current_value, depth):

        deep_indent_size = depth * spaces_count
        left_shift = replacer * (deep_indent_size - 2)
        current_indent = ((spaces_count * depth) - spaces_count) * replacer
        lines = []
        if isinstance(current_value, list):
            for i in current_value:
                match i['type']:
                    case 'nested':
                        lines.append(f"{left_shift}  {i['key']}: "
                                     f"{iter_(i['value'], depth + STEP)}")
                    case 'added':
                        lines.append(f"{left_shift}+ {i['key']}: "
                                     f"{to_str(i['value'], depth + STEP)}")
                    case 'removed':
                        lines.append(f"{left_shift}- {i['key']}: "
                                     f"{to_str(i['value'], depth + STEP)}")
                    case 'equal':
                        lines.append(f"{left_shift}  {i['key']}: "
                                     f"{to_str(i['value'], depth + STEP)}")
                    case 'updated':
                        lines.append(f"{left_shift}- {i['key']}: "
                                     f"{to_str(i['value1'], depth + STEP)}")
                        lines.append(f"{left_shift}+ {i['key']}: "
                                     f"{to_str(i['value2'], depth + STEP)}")
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, STEP)


def to_str(value, depth=0, replacer=' ', spaces_count=4):
    deep_indent_size = depth * spaces_count
    deep_indent = replacer * deep_indent_size
    current_indent = ((spaces_count * depth) - spaces_count) * replacer
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            if isinstance(v, dict):
                lines.append(f"{deep_indent}{k}: "
                             f"{to_str(v, depth + STEP)}")
            else:
                lines.append(f"{deep_indent}{k}: {to_str(v)}")
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
