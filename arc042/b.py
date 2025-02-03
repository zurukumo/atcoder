import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

x0, y0 = map(int, input().split())
N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]


def dist(x, y):
    return (x**2 + y**2) ** 0.5


ret = float("inf")
for i in range(N):
    xa, ya = xy[i - 1]
    xb, yb = xy[i]

    if xa == xb:
        if min(ya, yb) <= y0 <= max(ya, yb):
            ret = min(ret, abs(x0 - xa))
        else:
            ret = min(ret, dist(x0 - xa, y0 - ya), dist(x0 - xb, y0 - yb))
    elif ya == yb:
        if min(xa, xb) <= x0 <= max(xa, xb):
            ret = min(ret, abs(y0 - ya))
        else:
            ret = min(ret, dist(x0 - xa, y0 - ya), dist(x0 - xb, y0 - yb))
    else:
        f = lambda x: -(xb - xa) * (x - x0) / (yb - ya) + y0
        if (f(xa) - ya) * (f(xb) - yb) < 0:
            a = yb - ya
            b = -(xb - xa)
            c = -xa * yb + xb * ya
            ret = min(ret, abs(a * x0 + b * y0 + c) / ((a**2 + b**2) ** 0.5))
        else:
            ret = min(ret, dist(x0 - xa, y0 - ya), dist(x0 - xb, y0 - yb))

print(ret)
