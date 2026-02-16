import copy
shared = []
d = {"a": shared, "b": shared}
d["a"].append(1)
print(d)
#Fix
shared=[]
d={"a":copy.deepcopy(shared),"b": copy.deepcopy(shared)}
d["a"].append(1)
print(d)

