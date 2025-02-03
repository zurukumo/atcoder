from math import atan2, pi

N = int(input())
dxy = []
for _ in range(N):
    x, y = map(int, input().split())
    dxy.append((atan2(y, x), x, y))

dxy.sort()
for i in range(N):
    dxy.append((dxy[i][0] + 2 * pi, dxy[i][1], dxy[i][2]))

M = 0
E = 1e-6
for i in range(N):
    d, x, y = dxy[i][0], 0, 0
    for j in range(i, 2 * N):
        if dxy[j][0] - d > pi + E:
            break
        x += dxy[j][1]
        y += dxy[j][2]
        M = max(M, x * x + y * y)
print(M**0.5)
