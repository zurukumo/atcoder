from math import atan2, sin, cos, pi
N = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())

xc, yc = (x0 + x1) / 2, (y0 + y1) / 2
r = ((x0 - xc) ** 2 + (y0 - yc) ** 2) ** 0.5

rad = atan2(y0 - yc, x0 - xc)
rad += 2 * pi / N
print(xc + r * cos(rad), yc + r * sin(rad))