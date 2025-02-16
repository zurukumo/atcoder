import bisect

N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())
LRX = [[int(i) for i in input().split()] for _ in range(Q)]

pos = [[] for _ in range(N + 1)]
for i, a in enumerate(A):
    pos[a].append(i)

for l, r, x in LRX:
    l -= 1
    r -= 1
    print(bisect.bisect_left(pos[x], r + 1) - bisect.bisect_left(pos[x], l))
