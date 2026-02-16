a = [[1, 2], [3, 4]]
# a[1].append(7)

b = a.copy()
b[1].append(7)
c = a[:]
print(a)
print(b)
print(c)