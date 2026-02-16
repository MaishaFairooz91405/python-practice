# # scores = {"Alice":90, "Bob":75, "Tom":95}
# #
# # leaderboard = sorted(scores.values(), reverse=True)
# #
# # print(leaderboard)
#
# scores = {"Alice":90, "Bob":75, "Tom":95}
# # sorted_dict={}
# list1=[]
# for x in scores.values():
#     list1.append(x)
# value=max(list1)
# for y in scores.keys():
#     prin

scores = { "Maisha": 87, "Neha": 70,"Sumu": 84,"Subah": 90,"Megha": 91, "Puspita": 76}

items = list(scores.items())

# Step 2: manual sorting (descending by score)
n = len(items)

for i in range(n):
    for j in range(0, n-1):
        if items[j][1] < items[j+1][1]:   # compare scores
            items[j], items[j+1] = items[j+1], items[j]   # swap

# Step 3: print leaderboard
print("Leaderboard:")

for name, score in items:
    print(name, score)
