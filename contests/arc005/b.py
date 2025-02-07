x, y, W = input().split()
x, y = int(x) - 1, int(y) - 1
c = [[int(i) for i in input()] for _ in range(9)]

d = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

dx, dy = 0, 0
for w in W:
    dx += d[w][0]
    dy += d[w][1]

ret = []
for _ in range(4):
    ret.append(c[y][x])
    x += dx
    y += dy
    if x == -1:
        x, dx = 1, 1
    elif x == 9:
        x, dx = 7, -1
    if y == -1:
        y, dy = 1, 1
    elif y == 9:
        y, dy = 7, -1
print("".join(map(str, ret)))
