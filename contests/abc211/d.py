import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]
mod = 10**9 + 7

vec = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    vec[a].append(b)
    vec[b].append(a)


dist = [(float("inf"), 0) for _ in range(N)]
dist[0] = (0, 1)
queue = [(0, 0)]
while queue:
    ccost, cur = heapq.heappop(queue)
    ncost = ccost + 1
    for nex in vec[cur]:
        if dist[nex][0] == ncost:
            npattern = (dist[nex][1] + dist[cur][1]) % mod
            dist[nex] = (dist[nex][0], npattern)
        elif ncost < dist[nex][0]:
            dist[nex] = (ncost, dist[cur][1])
            heapq.heappush(queue, (ncost, nex))

print(dist[-1][1])
