import copy
a=[23,[10,65],65,[98,54]]
b=copy.deepcopy(a)

a[3].append(39)
print(a)
print(b)