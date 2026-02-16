votes = {}

names = ["A", "B", "A", "C", "A", "B"]

for name in names:
    votes[name] = votes.get(name, 0)
    votes[name] += 1


winner = max(votes, key=votes.get)

print("Votes:", votes)
print("Winner:", winner)
