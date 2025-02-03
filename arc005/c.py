H, W = map(int, input().split())
c = [input() for _ in range(H)]

for y in range(H):
    for x in range(W):
        if c[y][x] == "s":
            sx, sy = x, y
        if c[y][x] == "g":
            gx, gy = x, y


def bfs(y, x):
    q = [(y, x)]
    while q:
        y, x = q.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (
                0 <= ny < H
                and 0 <= nx < W
                and c[ny][nx] != "#"
                and visited[ny][nx] == -1
            ):
                q.append((ny, nx))
                visited[ny][nx] = 0


visited = [[-1] * W for _ in range(H)]
visited[sy][sx] = 0

bfs(sy, sx)

for y in range(H):
    for x in range(W):
        if visited[y][x] == -1 or visited[y][x] == 1:
            continue

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (
                0 <= ny < H
                and 0 <= nx < W
                and c[ny][nx] == "#"
                and visited[ny][nx] == -1
            ):
                visited[ny][nx] = 1

for y in range(H):
    for x in range(W):
        if visited[y][x] == 1:
            bfs(y, x)

for y in range(H):
    for x in range(W):
        if visited[y][x] == -1 or visited[y][x] == 2:
            continue

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (
                0 <= ny < H
                and 0 <= nx < W
                and c[ny][nx] == "#"
                and visited[ny][nx] == -1
            ):
                visited[ny][nx] = 2

for y in range(H):
    for x in range(W):
        if visited[y][x] == 2:
            bfs(y, x)

if visited[gy][gx] >= 0:
    print("YES")
else:
    print("NO")
