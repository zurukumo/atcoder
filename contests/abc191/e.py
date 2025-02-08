from heapq import heappop, heappush

N, M = map(int, input().split())
ABC = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[] for _ in range(N)]
for A, B, C in ABC:
    A, B = A - 1, B - 1
    vec[A].append((C, B))

for i in range(N):
    vec[i].sort()

dists = []
for cur in range(N):
    dist = [float("inf")] * N
    q = [(0, cur)]
    while q:
        ccost, cur = heappop(q)
        if ccost > dist[cur]:
            continue

        for ncost, nex in vec[cur]:
            if ccost + ncost < dist[nex]:
                dist[nex] = ccost + ncost
                heappush(q, (ccost + ncost, nex))

    dists.append(dist)

for i in range(N):
    ret = dists[i][i]

    if ret != float("inf"):
        print(ret)
    else:
        print(-1)
