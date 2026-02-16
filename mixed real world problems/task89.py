list1=[2,2,3,5,5,7,7,8,1,9]
list2=[]

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)