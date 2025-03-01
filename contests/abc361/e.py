import collections

N = int(input())
ABC = [[int(i) for i in input().split()] for _ in range(N - 1)]

ret = 0

graph = [[] for _ in range(N)]
for a, b, c in ABC:
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))
    ret += c * 2

queue = collections.deque([0])
dist = [-1] * N
dist[0] = 0
while queue:
    cur = queue.popleft()
    for nex, c in graph[cur]:
        if dist[nex] != -1:
            continue
        dist[nex] = dist[cur] + c
        queue.append(nex)

M = max(dist)
idx = dist.index(M)
queue = collections.deque([idx])
dist = [-1] * N
dist[idx] = 0
while queue:
    cur = queue.popleft()
    for nex, c in graph[cur]:
        if dist[nex] != -1:
            continue
        dist[nex] = dist[cur] + c
        queue.append(nex)

print(ret - max(dist))
