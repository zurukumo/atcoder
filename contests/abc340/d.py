import heapq

N = int(input())
ABX = [[int(i) for i in input().split()] for _ in range(N - 1)]

graph = [[] for _ in range(N)]
for i, (a, b, x) in enumerate(ABX):
    graph[i].append((i + 1, a))
    graph[i].append((x - 1, b))

queue = [(0, 0)]
cost = [float("inf")] * N
cost[0] = 0
while queue:
    cc, cur = heapq.heappop(queue)
    for nex, dc in graph[cur]:
        if cc + dc < cost[nex]:
            cost[nex] = cc + dc
            heapq.heappush(queue, (cost[nex], nex))

print(cost[-1])
