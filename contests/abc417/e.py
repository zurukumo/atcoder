import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(M)]

    vec = [[] for _ in range(N)]
    for u, v in UV:
        vec[u - 1].append(v - 1)
        vec[v - 1].append(u - 1)

    for i in range(N):
        vec[i].sort()

    X -= 1
    Y -= 1
    dist = [[N + 1] for _ in range(N)]
    queue = [([X], X)]
    dist[X] = [X]
    while queue:
        ccost, cur = heapq.heappop(queue)
        if cur == Y:
            break
        if ccost > dist[cur]:
            continue

        for nex in vec[cur]:
            ncost = ccost + [nex]
            if ncost < dist[nex]:
                heapq.heappush(queue, (ncost, nex))
                dist[nex] = ncost

    print(*(i + 1 for i in dist[Y]))
