import json


def generate_diff(file1, file2):
    with open(file1, 'r') as fp:
        data1 = json.load(fp)

    with open(file2, 'r') as fp:
        data2 = json.load(fp)

    sorted_data1 = dict(sorted(data1.items()))
    sorted_data2 = dict(sorted(data2.items()))
    container = []

    for key in sorted_data1:
        if key in sorted_data2 and sorted_data1[key] == sorted_data2[key]:
            container.append(f'    {key}: {sorted_data1[key]}')
        elif key in sorted_data2 and sorted_data1[key] != sorted_data2[key]:
            container.append(f'  - {key}: {sorted_data1[key]}')
            container.append(f'  + {key}: {sorted_data2[key]}')
        else:
            container.append(f'  - {key}: {sorted_data1[key]}')
    for key in sorted_data2:
        if key in sorted_data2 and key not in sorted_data1:
            container.append(f'  + {key}: {sorted_data2[key]}')

    container.append('}')
    container.insert(0, '{')
    print('\n'.join(container))
    return '\n'.join(container)
