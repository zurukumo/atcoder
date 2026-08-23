import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
uv = [[int(i) for i in input().split()] for _ in range(N - 1)]

vec = [[] for _ in range(N)]
for u, v in uv:
    vec[u - 1].append(v - 1)
    vec[v - 1].append(u - 1)

queue = collections.deque([])
dist = [float("inf")] * N
for i in range(N):
    if len(vec[i]) == 1 and dist[vec[i][0]] != 0:
        queue.append((0, vec[i][0]))
        dist[vec[i][0]] = 0

while queue:
    ccost, cur = queue.popleft()
    if ccost > dist[cur]:
        continue
    if ccost == 3:
        ccost = 0
        dist[cur] = 0

    for nex in vec[cur]:
        ncost = ccost + 1
        if ncost < dist[nex]:
            queue.append((ncost, nex))
            dist[nex] = ncost

ret = []
for i in range(N):
    if dist[i] == 0:
        cnt = 0
        for j in vec[i]:
            if dist[j] != 0:
                cnt += 1
        ret.append(cnt)

ret.sort()
print(*ret)
