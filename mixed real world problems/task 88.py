var_one="Maisha lives in kallyanpur and works in banani"
var_two=var_one.split()
dict1={}
for i in range(len(var_two)):
    if var_two[i] in dict1:
        dict1[var_two[i]]=dict1[var_two[i]]+1
    else:
        dict1[var_two[i]]=1

print(dict1)