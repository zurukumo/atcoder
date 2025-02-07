import heapq

N, M = map(int, input().split())
ABC = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[] for _ in range(N)]
for i, (A, B, C) in enumerate(ABC):
    vec[A - 1].append((B - 1, C, i))
    vec[B - 1].append((A - 1, C, i))

queue = [(0, 0, None)]
dp = [float("inf")] * N
ret = set()
while queue:
    cost, node, path = heapq.heappop(queue)
    if cost > dp[node]:
        continue

    if path is not None:
        ret.add(path + 1)

    for next_node, next_cost, next_path in vec[node]:
        if cost + next_cost < dp[next_node]:
            dp[next_node] = cost + next_cost
            heapq.heappush(queue, (cost + next_cost, next_node, next_path))

print(*ret)
