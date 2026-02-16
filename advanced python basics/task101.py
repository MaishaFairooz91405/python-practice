def safe_copy(data):
    new_dict = {}
    for k, v in data.items():
        # new_dict[k] = v[:]
        new_dict[k]=v.copy()
    return new_dict


data = {"a": [1, 2], "b": [3, 4]}
new_data = safe_copy(data)

new_data["a"].append(99)


print(data)      # unchanged
print(new_data)
