H, W = map(int, input().split())
S = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]
ret = 0
for y in range(H):
    for x in range(W):
        if visited[y][x] or S[y][x] == ".":
            continue

        queue = [(y, x)]
        visited[y][x] = True
        ret += 1
        while queue:
            cy, cx = queue.pop()
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and S[ny][nx] == "#":
                        visited[ny][nx] = True
                        queue.append((ny, nx))

print(ret)
