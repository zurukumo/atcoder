N, C = map(int, input().split())
D = [[int(i) for i in input().split()] for _ in range(C)]
c = [[int(i) for i in input().split()] for _ in range(N)]

ccount = [[0] * C for _ in range(3)]
for y in range(N):
    for x in range(N):
        ccount[(x + y) % 3][c[y][x] - 1] += 1

ccost = [[0] * C for _ in range(3)]
for i, cc in enumerate(ccount):
    m = float("inf")
    for j in range(C):
        ccost[i][j] = sum([cc[k] * D[k][j] for k in range(C)])

ret = float("inf")
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            ret = min(ret, ccost[0][i] + ccost[1][j] + ccost[2][k])
print(ret)
