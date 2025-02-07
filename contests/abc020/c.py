H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

for y in range(H):
    for x in range(W):
        if s[y][x] == "S":
            sy, sx = y, x
        if s[y][x] == "G":
            gy, gx = y, x


def check(m):
    dist = [[float("inf")] * W for _ in range(H)]
    dist[sy][sx] = 0
    q = [(sy, sx, 0)]
    while q:
        cy, cx, cco = q.pop()
        if dist[cy][cx] < cco:
            continue
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W:
                if s[ny][nx] == "#":
                    nco = cco + m
                else:
                    nco = cco + 1
                if nco < dist[ny][nx]:
                    dist[ny][nx] = nco
                    q.append((ny, nx, nco))
    return dist[gy][gx] <= T


ok, ng = 0, 10**12
while ng - ok > 1:
    m = (ok + ng) // 2
    if check(m):
        ok = m
    else:
        ng = m

print(ok)
