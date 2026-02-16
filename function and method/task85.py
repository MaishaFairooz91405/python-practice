def common_elements(list1,list2):
    list1=set(list1)
    list2=set(list2)
    list3=list1.intersection(list2)
    return list3

list1=[2,5,8,7,9,6]
list2=[5,10,8,3,21,6]
print(common_elements(list1,list2))