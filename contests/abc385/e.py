import heapq

N = int(input())
uv = [[int(i) for i in input().split()] for _ in range(N - 1)]

graph = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

ret = -float("inf")
for i in range(N):
    hq = []
    for j in graph[i]:
        heapq.heappush(hq, len(graph[j]))
    while hq:
        x = len(hq)
        y = hq[0]
        ret = max(ret, x * y)
        heapq.heappop(hq)

print(N - 1 - ret)
