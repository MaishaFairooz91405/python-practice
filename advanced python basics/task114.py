# def modify(list_one):
#     print(id(list_one))
#     list_one.append(5)
#     print(id(list_one))
#
# list_one=[21,32,45]
# modify(list_one)
#
def list_rebinding(list_one):
    print(id(list_one))
    list_one=list_one+[56]
    print(id(list_one))
list_one=[21,32,45]
list_rebinding(list_one)