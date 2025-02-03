from itertools import combinations

ABCDE = [int(i) for i in input().split()]

s = []

for comb in combinations(ABCDE, 3) :
    s.append(sum(comb))
    
s = list(set(s))
s.sort()
print(s[-3])