from itertools import permutations

N = int(input())
P = tuple(int(i) for i in input().split())
Q = tuple(int(i) for i in input().split())

perm = list(permutations(range(1, N + 1)))

a = 0
b = 0

for i, p in enumerate(perm):
    if p == P:
        a = i + 1
    if p == Q:
        b = i + 1

print(abs(a - b))
