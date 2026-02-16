import copy
# a=[76,54,32,21,10]
# b=copy.deepcopy(a)
# a[3]=98
# print(a)
# print(b)

a=[76,54,32,21,10]
b=a.copy()
a.append(98)
print(a)
print(b)