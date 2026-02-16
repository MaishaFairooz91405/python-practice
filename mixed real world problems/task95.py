def unique_elements(*args):
    result = list(set(a) | set(b) | set(c))
    result1 = list(set(a) & set(b) & set(c))
    for i in result1:
        print(i)
    result.remove(i)
    return result
a=[1,2]
b=[2,3]
c=[2,5]
print(unique_elements(a,b,c))

# a=[1,2]
# b=[2,3]
# c=[2,5]
# result  = list(set(a)|set(b) | set(c))
# result1=list(set(a) &set(b) & set(c))
# for i in result1:
#     print(i)
# result.remove(i)
# print(result)

# def unique_elements(*lists):
#     unique = set()
#     for i in lists:
#        unique.update(i)
#     return list(unique)
#
# print(unique_elements([21,32,45],[21,87,45],[50,76,78]))
