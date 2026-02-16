def compare(a, b):
    if a is b:
        print("same object")
    elif a == b:
        print("same value")
    else:
        print("different")

# value1=259
# value2=value1
list1=[1,2]
list2=[1,2]
# compare(list1,list2)
tup_one = ('a','c')
tup_two = ('a','c')
compare(tup_one,tup_two)