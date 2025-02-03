from itertools import combinations

S = input()

ret = 0
for i in range(len(S)):
    for comb in combinations(range(1, len(S)), i):
        comb = [0] + list(comb) + [len(S)]
        for i in range(1, len(comb)):
            ret += int(S[comb[i - 1] : comb[i]])

print(ret)
