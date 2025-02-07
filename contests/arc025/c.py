import sys

input = sys.stdin.readline
from heapq import heappush, heappop

N, M, R, T = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    vec[a - 1].append((b - 1, c))
    vec[b - 1].append((a - 1, c))

INF = 1 << 30

ret = 0
for C in range(N):
    dist = [INF] * N
    queue = [(0, C)]
    dist[C] = 0

    while queue:
        ccost, cur = heappop(queue)
        if dist[cur] < ccost:
            continue
        for nex, ncost in vec[cur]:
            if ccost + ncost < dist[nex]:
                heappush(queue, (ccost + ncost, nex))
                dist[nex] = ccost + ncost

    dist.sort()
    r = 1
    for B in range(1, N):
        while r < N and dist[r] * T <= dist[B] * R:
            r += 1
        if r == N:
            break
        ret += N - r

if T > R:
    ret -= N * (N - 1)

print(ret)
