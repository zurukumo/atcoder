H, W = map(int, input().split())
S = [input() for _ in range(H)]

mod = 998244353

group = [[-1] * W for _ in range(H)]
c = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            continue
        if group[y][x] != -1:
            continue

        queue = [(y, x)]
        group[y][x] = c
        while queue:
            cy, cx = queue.pop()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "#" and group[ny][nx] == -1:
                    group[ny][nx] = c
                    queue.append((ny, nx))
        c += 1

ret = 0
red = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            red += 1
            neighbors = set()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny = y + dy
                nx = x + dx
                if 0 <= ny < H and 0 <= nx < W and group[ny][nx] != -1:
                    neighbors.add(group[ny][nx])
            ret += c - len(neighbors) + 1


ret *= pow(red, mod - 2, mod)
ret %= mod

print(ret)
