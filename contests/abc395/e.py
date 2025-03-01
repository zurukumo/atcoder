import heapq

N, M, X = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[] for _ in range(N * 2)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append((v, 1))
    graph[v + N].append((u + N, 1))
for i in range(N):
    graph[i].append((i + N, X))
    graph[i + N].append((i, X))

queue = [(0, 0)]
dist = [float("inf")] * (N * 2)
dist[0] = 0
while queue:
    d, u = heapq.heappop(queue)
    if dist[u] < d:
        continue
    for v, c in graph[u]:
        if dist[u] + c < dist[v]:
            dist[v] = dist[u] + c
            heapq.heappush(queue, (dist[v], v))

print(min(dist[N - 1], dist[2 * N - 1]))
