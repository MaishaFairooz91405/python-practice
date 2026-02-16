list1=[11,16,22,25,44,34,37,68,98,87]
result={"even":[],"odd":[]}
for i in list1:
    if i%2==0:
        result["even"].append(i)
    else:
       result["odd"].append(i)
print(result)