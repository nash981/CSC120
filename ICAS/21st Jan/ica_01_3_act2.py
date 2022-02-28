def max_key_by_val(data):
    pairs = []
    for keys,values in data.items():
        pairs.append((values,keys))
    pairs = sorted(pairs)
    return pairs[-1][1]