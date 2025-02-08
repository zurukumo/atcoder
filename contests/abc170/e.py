import sys

input = sys.stdin.readline
from heapq import heappop, heappush

N, Q = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]
CD = [[int(i) for i in input().split()] for _ in range(Q)]

M = 2 * (10**5) + 10
kinder = [[] for _ in range(M)]

for i, (A, B) in enumerate(AB):
    heappush(kinder[B], (-A, i + 1))

last = [-1] * M
rank = []
for i in range(M):
    if kinder[i]:
        heappush(rank, (-kinder[i][0][0], i, -1))

for i, (C, D) in enumerate(CD):
    pos = AB[C - 1][1]
    heappush(kinder[D], (-AB[C - 1][0], C))
    AB[C - 1][1] = D
    while kinder[D] and AB[kinder[D][0][1] - 1][1] != D:
        heappop(kinder[D])
    while kinder[pos] and AB[kinder[pos][0][1] - 1][1] != pos:
        heappop(kinder[pos])
    if kinder[D]:
        heappush(rank, (-kinder[D][0][0], D, i))
    if kinder[pos]:
        heappush(rank, (-kinder[pos][0][0], pos, i))
    last[D] = i
    last[pos] = i
    while rank and rank[0][2] < last[rank[0][1]]:
        heappop(rank)
    print(rank[0][0])
