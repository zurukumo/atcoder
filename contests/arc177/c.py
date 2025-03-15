import heapq

N = int(input())
C = [input() for _ in range(N)]

ret = 0

queue = [(C[0][0] == "B", 0, 0)]
cost1 = [[float("inf")] * N for _ in range(N)]
cost1[0][0] = C[0][0] == "B"
while queue:
    cos, cy, cx = heapq.heappop(queue)
    if cos > cost1[cy][cx]:
        continue
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = cy + dy, cx + dx
        if 0 <= nx < N and 0 <= ny < N:
            ncos = cos + (C[ny][nx] == "B")
            if ncos < cost1[ny][nx]:
                cost1[ny][nx] = ncos
                heapq.heappush(queue, (ncos, ny, nx))

queue = [(C[N - 1][0] == "R", N - 1, 0)]
cost2 = [[float("inf")] * N for _ in range(N)]
cost2[N - 1][0] = C[N - 1][0] == "R"
while queue:
    cos, cy, cx = heapq.heappop(queue)
    if cos > cost2[cy][cx]:
        continue
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = cy + dy, cx + dx
        if 0 <= nx < N and 0 <= ny < N:
            ncos = cos + (C[ny][nx] == "R")
            if ncos < cost2[ny][nx]:
                cost2[ny][nx] = ncos
                heapq.heappush(queue, (ncos, ny, nx))

print(cost1[N - 1][N - 1] + cost2[0][N - 1])
