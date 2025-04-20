import collections

import sortedcontainers

H, W, rs, cs = map(int, input().split())
N = int(input())
rc = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
dl = [input().split() for _ in range(Q)]

xy = collections.defaultdict(lambda: sortedcontainers.SortedList())
yx = collections.defaultdict(lambda: sortedcontainers.SortedList())

for r, c in rc:
    xy[c].add(r)
    xy[c].add(0)
    xy[c].add(H + 1)
    yx[r].add(c)
    yx[r].add(0)
    yx[r].add(W + 1)

x = cs
y = rs
for d, l in dl:
    l = int(l)
    if d == "L":
        if y in yx:
            i = yx[y][yx[y].bisect_left(x) - 1]
        else:
            i = 0
        if i >= x - l:
            x = i + 1
        else:
            x = x - l
    elif d == "R":
        if y in yx:
            i = yx[y][yx[y].bisect_right(x)]
        else:
            i = W + 1
        if i <= x + l:
            x = i - 1
        else:
            x = x + l
    elif d == "U":
        if x in xy:
            i = xy[x][xy[x].bisect_left(y) - 1]
        else:
            i = 0
        if i >= y - l:
            y = i + 1
        else:
            y = y - l
    elif d == "D":
        if x in xy:
            i = xy[x][xy[x].bisect_right(y)]
        else:
            i = H + 1
        if i <= y + l:
            y = i - 1
        else:
            y = y + l

    print(y, x)
