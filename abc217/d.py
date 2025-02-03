import sortedcontainers

L, Q = map(int, input().split())
cx = [[int(i) for i in input().split()] for _ in range(Q)]

sl = sortedcontainers.SortedList()
sl.add(0)
sl.add(L)
for c, x in cx:
    if c == 1:
        sl.add(x)
    else:
        lidx = sl.bisect_left(x) - 1
        ridx = sl.bisect_right(x)
        print(sl[ridx] - sl[lidx])
