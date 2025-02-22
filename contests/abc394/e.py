import collections
import heapq

N = int(input())
C = [input() for _ in range(N)]

G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if C[i][j] == "-":
            continue
        G[i].append((j, C[i][j]))
        rG[j].append((i, C[i][j]))

queue = [(0, (i, i)) for i in range(N)]
ret = collections.defaultdict(lambda: float("inf"))
for i in range(N):
    ret[(i, i)] = 0
for i in range(N):
    for j in range(N):
        if C[i][j] != "-":
            ret[(i, j)] = min(ret[(i, j)], 1)
            heapq.heappush(queue, (1, (i, j)))

while queue:
    cost, v = heapq.heappop(queue)
    f1, t1 = v
    for f2, c1 in rG[f1]:
        for t2, c2 in G[t1]:
            if c1 == c2:
                if ret[(f2, t2)] > cost + 2:
                    ret[(f2, t2)] = cost + 2
                    heapq.heappush(queue, (cost + 2, (f2, t2)))

for i in range(N):
    print(*[-1 if ret[(i, j)] == float("inf") else ret[(i, j)] for j in range(N)])
