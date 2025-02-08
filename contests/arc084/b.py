from heapq import heappop, heappush

K = int(input())

queue = [(1, 1)]
dist = [float("inf")] * K
dist[1] = 1

while queue:
    cost, cur = heappop(queue)
    if cost + 1 < dist[(cur + 1) % K]:
        dist[(cur + 1) % K] = cost + 1
        heappush(queue, (cost + 1, (cur + 1) % K))
    if cost < dist[cur * 10 % K]:
        dist[cur * 10 % K] = cost
        heappush(queue, (cost, cur * 10 % K))

print(dist[0])
