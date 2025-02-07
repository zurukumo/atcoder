import heapq

H, W, Y = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]

queue = []
visited = [[0] * W for _ in range(H)]

init = set()
for y in range(H):
    init.add((y, 0))
    init.add((y, W - 1))
for x in range(W):
    init.add((0, x))
    init.add((H - 1, x))

for y, x in init:
    heapq.heappush(queue, (A[y][x], (y, x)))
    visited[y][x] = 1

ret = H * W
for depth in range(1, Y + 1):
    while queue and queue[0][0] <= depth:
        _, (y, x) = heapq.heappop(queue)
        ret -= 1
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
                heapq.heappush(queue, (max(depth, A[ny][nx]), (ny, nx)))
                visited[ny][nx] = 1
    print(ret)
