H, W = map(int, input().split())
C = [[0] * (W + 1) for _ in range(H + 1)]
for y in range(H):
    for x, v in enumerate(map(int, input().split())):
        C[y + 1][x + 1] = v

for y in range(H + 1):
    for x in range(W + 1):
        if (y + x) & 1:
            C[y][x] *= -1

for y in range(1, H + 1):
    for x in range(1, W + 1):
        C[y][x] += C[y - 1][x] + C[y][x - 1] - C[y - 1][x - 1]

ret = 0
for fy in range(H + 1):
    for fx in range(W + 1):
        for gy in range(H, fy, -1):
            if (gy - fy) * (W - fx) < ret:
                break
            for gx in range(W, fx, -1):
                if (gy - fy) * (gx - fx) < ret:
                    break
                if C[fy][fx] + C[gy][gx] - C[fy][gx] - C[gy][fx] == 0:
                    ret = max(ret, (gy - fy) * (gx - fx))

print(ret)
