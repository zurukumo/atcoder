from math import sin, cos, pi

A, B, H, M = map(int, input().split())

r1 = 2 * pi * (60 * H + M) / (12 * 60)
x1, y1 = A * cos(r1), A * sin(r1)

r2 = 2 * pi * M / 60
x2, y2 = B * cos(r2), B * sin(r2)

diff = (x1 - x2) ** 2 + (y1 - y2) ** 2
print(diff**0.5)
