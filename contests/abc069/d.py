H, W = map(int, input().split())
N = int(input())
a = []
for i, ai in enumerate(map(int, input().split())):
    for _ in range(ai):
        a.append(i + 1)
a = a[::-1]

c = [[0] * W for _ in range(H)]

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
di = 0
dx, dy = d[0]
x, y = 0, 0
for i in range(H * W):
    c[y][x] = a.pop()
    if not (0 <= x + dx < W) or not (0 <= y + dy < H) or c[y + dy][x + dx] != 0:
        di = (di + 1) % 4

    dx, dy = d[di]
    x += dx
    y += dy

for i in range(H):
    print(*c[i])
