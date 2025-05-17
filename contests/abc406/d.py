import sortedcontainers

H, W, N = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())

rows = [sortedcontainers.SortedList() for _ in range(H)]
cols = [sortedcontainers.SortedList() for _ in range(W)]

for x, y in XY:
    x -= 1
    y -= 1
    rows[x].add(y)
    cols[y].add(x)

for _ in range(Q):
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        _, x = query
        x -= 1
        print(len(rows[x]))
        for y in rows[x]:
            cols[y].remove(x)
        rows[x].clear()
    else:
        _, y = query
        y -= 1
        print(len(cols[y]))
        for x in cols[y]:
            rows[x].remove(y)
        cols[y].clear()
