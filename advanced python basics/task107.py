def same_reference(a, b):
    return id(a) == id(b)

lst1 = [1, 2, 3]
lst2 = lst1

print("Test 1:", same_reference(lst1, lst2))

lst3 = [1, 2, 3]
lst4 = [1, 2, 3]

print("Test 2:", same_reference(lst3, lst4))

a = 10
b = 10
print("Test 3:", same_reference(a, b))

x = 1000
y = 1000
print("Test 4:", same_reference(x, y))

t1 = (1, 2)
t2 = t1
print("Test 5:", same_reference(t1, t2))
