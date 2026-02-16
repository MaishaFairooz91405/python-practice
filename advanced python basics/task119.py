import copy
def snapshot(list1):
     return copy.deepcopy(list1)

def live_reference(list1):
    return list1

list1 = [1, 2, 3]

snapshot_list1 = snapshot(list1)
live_list1 = live_reference(list1)

print("Before change:")
print("original:", list1)
print("snapshot:", snapshot_list1)
print("live:", live_list1)

list1.append(67)
print("Before change:")
print("original:", list1)
print("snapshot:", snapshot_list1)
print("live:", live_list1)