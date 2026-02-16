def deep_merge_dicts(d1: dict, d2: dict) -> dict:
    final_dict={}
    keys_d1=d1.keys()
    keys_d2=d2.keys()
    final_keys=set(keys_d1) | set(keys_d2)
    # print(final_keys)
    for i in final_keys:
        if i in keys_d1 and i in keys_d2:
            if isinstance(d1[i],dict) and isinstance(d2[i],dict):
                final_dict[i]=deep_merge_dicts(d1[i],d2[i])
            else:
                final_dict[i]=d2[i]

        elif i in d1:
            final_dict[i]=d1[i]
        else:
            final_dict[i]=d2[i]
    return final_dict
d1 = {
    "a": 1,
    "b": {
        "x": 10,
        "y": 20
    },
    "c": 3
}
d2 = {
    "b": {
        "y": 99,
        "z": 50
    },
    "d": 4
}
print(deep_merge_dicts(d1,d2))

