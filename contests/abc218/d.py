import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

points = set()
for x, y in xy:
    points.add((x, y))

s = 0
for i in range(N):
    for j in range(i):
        xi, yi = xy[i]
        xj, yj = xy[j]
        if xi == xj or yi == yj:
            continue
        xk, yk = xi, yj
        xl, yl = xj, yi
        if (xk, yk) in points and (xl, yl) in points:
            s += 1

print(s // 2)
