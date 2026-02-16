def return_list(list1):
    list2=list1.copy()
    list2.append(40)
    return list2

list1=[21,76,54,98,70]
print(return_list(list1))
print(list1)