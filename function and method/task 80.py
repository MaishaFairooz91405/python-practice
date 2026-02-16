# Using built in set
# def duplicates_removal(list1):
#     list1=set(list1)
#     return list1
#
# print(duplicates_removal([1,2,5,4,2,1,5]))

#Manually

def duplicates_removal(list1):
    list2=[]
    for i in range(len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])

    return list2
list1=[1,2,5,2,1,5,4,4,3]
print(duplicates_removal(list1))