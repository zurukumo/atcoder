import collections

import sortedcontainers

N, M, Sx, Sy = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(N)]
DC = [input().split() for _ in range(M)]

rows = collections.defaultdict(sortedcontainers.SortedList)
cols = collections.defaultdict(sortedcontainers.SortedList)


for X, Y in XY:
    rows[Y].add(X)
    cols[X].add(Y)

ret = 0
cx, cy = Sx, Sy
for d, c in DC:
    c = int(c)
    if d == "U":
        frY = cy
        toY = cy + c
        i = cols[cx].bisect_left(frY)
        while i < len(cols[cx]) and cols[cx][i] <= toY:
            ty = cols[cx][i]
            cols[cx].remove(ty)
            rows[ty].remove(cx)
            ret += 1
        cy = toY
    if d == "D":
        frY = cy
        toY = cy - c
        i = cols[cx].bisect_left(toY)
        while i < len(cols[cx]) and cols[cx][i] <= frY:
            ty = cols[cx][i]
            cols[cx].remove(ty)
            rows[ty].remove(cx)
            ret += 1
        cy = toY
    if d == "L":
        frX = cx
        toX = cx - c
        i = rows[cy].bisect_left(toX)
        while i < len(rows[cy]) and rows[cy][i] <= frX:
            tx = rows[cy][i]
            rows[cy].remove(tx)
            cols[tx].remove(cy)
            ret += 1
        cx = toX
    if d == "R":
        frX = cx
        toX = cx + c
        i = rows[cy].bisect_left(frX)
        while i < len(rows[cy]) and rows[cy][i] <= toX:
            tx = rows[cy][i]
            rows[cy].remove(tx)
            cols[tx].remove(cy)
            ret += 1
        cx = toX

print(cx, cy, ret)
