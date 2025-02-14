import collections

N, M = map(int, input().split())

graph = []

for i in range(N + 1):
    for j in range(N + 1):
        if i**2 + j**2 == M:
            graph.append((i, j))
            graph.append((-i, j))
            graph.append((i, -j))
            graph.append((-i, -j))

cost = [[-1] * N for _ in range(N)]
queue = collections.deque([(0, 0)])
cost[0][0] = 0

while queue:
    x, y = queue.popleft()
    for dx, dy in graph:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and cost[nx][ny] == -1:
            cost[nx][ny] = cost[x][y] + 1
            queue.append((nx, ny))

for row in cost:
    print(*row)
