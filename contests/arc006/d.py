H, W = map(int, input().split())
c = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]


def bfs(y, x):
    s = 1
    visited[y][x] = True

    q = [(y, x)]
    while q:
        cy, cx = q.pop()
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and c[ny][nx] == "o":
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    s += 1

    return s


ret = [0] * 3
for y in range(H):
    for x in range(W):
        if not visited[y][x] and c[y][x] == "o":
            s = bfs(y, x)

            # A12 B16 C11
            for i in range(1, 1001):
                if s == i * i * 12:
                    ret[0] += 1
                    break
                if s == i * i * 16:
                    ret[1] += 1
                    break
                if s == i * i * 11:
                    ret[2] += 1
                    break

print(*ret)
