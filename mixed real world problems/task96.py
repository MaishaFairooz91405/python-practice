a = [1,2,3,4]
b = [3,4,5]
c = [4,6,3]
d=set(a).intersection(set(b))
e=set(d).intersection(set(c))
print(list(e))
# result = list(set(a) & set(b) & set(c))
# print(result)
