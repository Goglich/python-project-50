def get_diff(data1, data2):
    differences = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        if key not in data2:
            differences.append({
                "key": key,
                "value": data1[key],
                "type": 'removed',
            })
            continue
        elif key not in data1:
            differences.append({
                "key": key,
                "value": data2[key],
                "type": 'added',
            })
            continue
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            differences.append({
                "key": key,
                "value": get_diff(data1[key], data2[key]),
                "type": 'nested',
            })
            continue
        elif data1[key] == data2[key]:
            differences.append({
                "key": key,
                "value": data1[key],
                "type": 'equal',
            })
            continue
        else:
            differences.append({
                "key": key,
                "value1": data1[key],
                "value2": data2[key],
                "type": 'updated',
            })
    return differences
