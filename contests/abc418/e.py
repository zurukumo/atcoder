from collections import defaultdict
from math import gcd

N = int(input())
XY = [[int(i) for i in input().split()] for _ in range(N)]


def gradient(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    if dx < 0:
        dx = -dx
        dy = -dy
    if dx == 0:
        return (0, 1)
    g = gcd(dx, abs(dy))

    return (dx // g, dy // g)


def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


gradient_cnt = defaultdict(int)
gradient_distance_cnt = defaultdict(int)
for i, (x1, y1) in enumerate(XY):
    for x2, y2 in XY[i + 1 :]:
        g = gradient(x1, y1, x2, y2)
        d = distance(x1, y1, x2, y2)
        gradient_cnt[g] += 1
        gradient_distance_cnt[(g, d)] += 1

ret = 0
for c in gradient_cnt.values():
    ret += c * (c - 1) // 2
dup = 0
for c in gradient_distance_cnt.values():
    dup += c * (c - 1) // 2
ret -= dup // 2

print(ret)
