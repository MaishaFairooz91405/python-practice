list1=[]
for i in range(1000):          #Time complexity: O(n) and it is slower because it is proportional to the input size
    list1.insert(0,i)
print(list1)


list1=[]
for i in range(1000):          #Time complexity : O(1)
    list1.append(i)
print(list1)