import copy
#List
class safeAPI_list:
    def __init__(self,list1):
        self.list1 = list1
    def get_list(self):
        return copy.deepcopy(self.list1)
    def add(self, item):
        self.list1.append(item)
    def remove(self, item):
        if item in self.list1:
            self.list1.remove(item)

print(" LIST API ")
list_one = safeAPI_list([1, 2, 3])
user_list = list_one.get_list()

user_list.append(999)
user_list.append(102)
user_list.remove(1)
print("User:", user_list)
print("Internal:", list_one.get_list())

# #Tuple
# class safeAPI_tuple:
#     def __init__(self,list1):
#         self.list1 =list1
#     def get_tuple(self):
#         return copy.deepcopy(tuple(self.list1))
#     def add(self, item):
#         self.list1.append(item)
#     def remove(self, item):
#         if item in self.list1:
#             self.list1.remove(item)
#
# print("Tuple API")
# tuple_one = safeAPI_tuple([68, 56, 47])
# user_tuple = tuple_one.get_tuple()
# user_tuple.append(999)
# user_tuple.remove(1)
# print("User:", user_tuple)
# print("Internal:", tuple_one.get_tuple())

#Dict
class safeAPI_Dict:
    def __init__(self,dict1):
        self.dict1 = dict1
    def get_dict(self):
        return copy.deepcopy(  self.dict1)
    def update(self,key,value):
        self.dict1[key] = value
    def remove_key(self, key):
       return self.dict1.pop(key,None)

print("\n------ DICT API ------")
dict_one= safeAPI_Dict({"abc": 58, "def": 89})
user_dict = dict_one.get_dict()

user_dict ["abc"] = 999
user_dict ["ghp"] = 789
print("User:", user_dict )
print("Internal:", dict_one.get_dict())

dict_one.remove_key("def")
print("User:", user_dict )
print("Internal:", dict_one.get_dict())
# # print("After set:", user_dict.get_dict())
# # print("Internal:", dict_one.get_dict())