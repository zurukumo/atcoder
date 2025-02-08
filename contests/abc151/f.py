import sys

input = sys.stdin.readline
from itertools import combinations
from math import sqrt

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]
E = 1e-9


def vnrm(v):
    d = sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
    for i in range(3):
        v[i] /= d

    return d


def vrot90(v):
    v0 = v[0]
    v[0] = -v[1]
    v[1] = v0


def calc(x1, y1, x2, y2, x3, y3):
    c = [0] * 3
    v123 = (x2 - x1) * (x3 - x2) + (y2 - y1) * (y3 - y2)
    v231 = (x3 - x2) * (x1 - x3) + (y3 - y2) * (y1 - y3)
    v312 = (x1 - x3) * (x2 - x1) + (y1 - y3) * (y2 - y1)

    if v123 < 0 and v231 < 0 and v312 < 0:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2
        v12 = [x2 - x1, y2 - y1, 0.0]
        vnrm(v12)
        vrot90(v12)
        x13 = (x1 + x3) / 2
        y13 = (y1 + y3) / 2
        v13 = [x3 - x1, y3 - y1, 0.0]
        vnrm(v13)
        vrot90(v13)
        d = -(v12[0] * v13[1] - v12[1] * v13[0])
        ds = -(x13 - x12) * v13[1] + (y13 - y12) * v13[0]
        s = ds / d
        c[0] = x12 + s * v12[0]
        c[1] = y12 + s * v12[1]
        c[2] = sqrt((x1 - c[0]) * (x1 - c[0]) + (y1 - c[1]) * (y1 - c[1]))

    else:
        if v123 >= 0:
            c[0] = (x1 + x3) / 2
            c[1] = (y1 + y3) / 2
            c[2] = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) / 2
        elif v231 >= 0:
            c[0] = (x1 + x2) / 2
            c[1] = (y1 + y2) / 2
            c[2] = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) / 2
        else:
            c[0] = (x2 + x3) / 2
            c[1] = (y2 + y3) / 2
            c[2] = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) / 2

    return c


ret = float("inf")
for i, j, k in combinations(range(N), 3):
    cx, cy, cr = calc(xy[i][0], xy[i][1], xy[j][0], xy[j][1], xy[k][0], xy[k][1])
    for x, y in xy:
        if sqrt((cx - x) ** 2 + (cy - y) ** 2) > cr + E:
            break
    else:
        ret = min(ret, cr)

if N == 2:
    r = sqrt((xy[0][0] - xy[1][0]) ** 2 + (xy[0][1] - xy[1][1]) ** 2)
    print(r / 2)

else:
    print(ret)
