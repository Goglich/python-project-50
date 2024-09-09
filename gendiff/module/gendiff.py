def generate_diff(data1, data2):
    sorted_data1 = data1
    sorted_data2 = data2
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
