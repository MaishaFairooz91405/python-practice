def modify(lst):
    lst.append(100)


nums = [1, 2, 3]
modify(nums)

print(nums)
#Code rewrite
import copy
def modify_safe(lst):
    new_lst = copy.deepcopy(lst)
    new_lst.append(100)
    return new_lst


nums = [1, 2, 3]
result = modify_safe(nums)

print(nums)
print(result)
