K = int(input())
S = input()

memo = dict()
# memo[x, y, dir]
# dir: 0, 1, 2, 3 = U, L, D, R
memo[(0, 0, 0)] = [0, 1]
memo[(0, 0, 1)] = [-1, 0]
memo[(0, 0, 2)] = [0, -1]
memo[(0, 0, 3)] = [1, 0]

convert = {v: i for i, v in enumerate("ULDR")}

x, y = 0, 0
for s in S:
    s = convert[s]
    x, y = memo[(x, y, s)]
    for i, (dx, dy) in enumerate(((0, 1), (-1, 0), (0, -1), (1, 0))):
        if not (x + dx, y + dy, i) in memo:
            memo[(x, y, i)] = [x + dx, y + dy]
        else:
            memo[(x, y, i)] = memo[(x + dx, y + dy, i)]
    for i, (dx, dy) in enumerate(((0, 1), (-1, 0), (0, -1), (1, 0))):
        nx, ny = memo[(x, y, i)]
        nx, ny = nx - dx, ny - dy
        memo[(nx, ny, (i + 2) % 4)] = memo[(x, y, (i + 2) % 4)]

print(x, y)
