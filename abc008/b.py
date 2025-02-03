N = int(input())
votes = {}
for _ in range(N):
    vote = input()
    if vote in votes:
        votes[vote] += 1
    else:
        votes[vote] = 1

print(max(votes, key=votes.get))
