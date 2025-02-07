N = int(input())
S = input()

winner = ""
cnt = {"T": 0, "A": 0}
for c in S:
    cnt[c] += 1
    if cnt["T"] > cnt["A"]:
        winner = "T"
    elif cnt["T"] < cnt["A"]:
        winner = "A"

print(winner)
