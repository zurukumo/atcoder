import heapq

N, M, K = map(int, input().split())
uva = [[int(i) for i in input().split()] for _ in range(M)]
s = [int(i) for i in input().split()]

graph = [[] for _ in range(2 * N)]
for u, v, a in uva:
    u -= 1
    v -= 1
    if a == 0:
        u += N
        v += N
    graph[u].append((v, 1))
    graph[v].append((u, 1))

for u in s:
    u -= 1
    graph[u].append((u + N, 0))
    graph[u + N].append((u, 0))


queue = [(0, 0)]
dist = [float("inf")] * (2 * N)
dist[0] = 0
while queue:
    cc, cur = heapq.heappop(queue)
    if dist[cur] < cc:
        continue
    for nex, nc in graph[cur]:
        if cc + nc < dist[nex]:
            dist[nex] = cc + nc
            heapq.heappush(queue, (cc + nc, nex))

if dist[N - 1] == float("inf") and dist[2 * N - 1] == float("inf"):
    print(-1)
else:
    print(min(dist[N - 1], dist[2 * N - 1]))
