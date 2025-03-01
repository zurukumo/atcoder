import heapq

N, X = map(int, input().split())
UD = [[int(i) for i in input().split()] for _ in range(N)]

cost = [float("inf")] * N
queue = []
for i, (u, d) in enumerate(UD):
    heapq.heappush(queue, (u, i))

while queue:
    u, i = heapq.heappop(queue)
    if u > cost[i]:
        continue
    cost[i] = u
    if i - 1 >= 0 and cost[i - 1] > u + X:
        heapq.heappush(queue, (u + X, i - 1))
        cost[i - 1] = u + X
    if i + 1 < N and cost[i + 1] > u + X:
        heapq.heappush(queue, (u + X, i + 1))
        cost[i + 1] = u + X

m = float("inf")
for i, (u, d) in enumerate(UD):
    m = min(m, cost[i] + d)

ret = sum(u + d for u, d in UD) - m * N
print(ret)
