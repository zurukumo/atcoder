from heapq import heappush, heappop

H, W = map(int, input().split())
s = [input() for _ in range(H)]

dist = [[float("inf")] * W for _ in range(H)]
q = [(0, 0, 0)]
while q:
    cost, cx, cy = heappop(q)
    if cost >= dist[cy][cx]:
        continue
    dist[cy][cx] = cost

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= cx + dx < W and 0 <= cy + dy < H and s[cy + dy][cx + dx] != "#":
            heappush(q, (cost + 1, cx + dx, cy + dy))

if dist[H - 1][W - 1] == float("inf"):
    print(-1)
else:
    ret = 0
    for s_ in s:
        ret += s_.count("#")
    print(H * W - ret - dist[H - 1][W - 1] - 1)
