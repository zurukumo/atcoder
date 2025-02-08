
N, M = map(int, input().split())
b = [[int(i) for i in input()] for _ in range(N)]

a = [[0] * M for _ in range(N)]

for y in range(1, N - 1):
    for x in range(1, M - 1):
        z = min(b[y - 1][x], b[y + 1][x], b[y][x - 1], b[y][x + 1])
        b[y - 1][x] -= z
        b[y + 1][x] -= z
        b[y][x - 1] -= z
        b[y][x + 1] -= z
        a[y][x] += z

for y in range(N):
    print("".join(map(str, a[y])))
