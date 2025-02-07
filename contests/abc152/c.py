from collections import defaultdict

N = int(input())
P = [int(i) for i in input().split()]

m = float("inf")
ret = 0
for i, p in enumerate(P):
    if p < m:
        ret += 1
        m = p

print(ret)
