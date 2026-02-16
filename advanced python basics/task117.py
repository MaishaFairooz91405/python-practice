import copy
# def get_data():
#     return internal
#
# internal = []
# x = get_data()
# x.append(1)
# print(x)
# print(internal)

#Fix
def get_data():
    return copy.deepcopy(internal)

internal = []
x = get_data()
x.append(1)
print(x)
print(internal)