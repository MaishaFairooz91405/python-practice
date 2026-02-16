def default_argument_problem(x,list1=None):
    if list1 is None:
        list1=[]
        list1.append(x)
    return list1

print(default_argument_problem(21))
print(default_argument_problem("Maisha"))
print(default_argument_problem(76))
print(default_argument_problem("Borsha"))