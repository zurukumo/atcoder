import sortedcontainers

Q = int(input())

sl = sortedcontainers.SortedList()
for _ in range(Q):
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        _, x = query
        sl.add(x)
    elif query[0] == 2:
        _, x, k = query
        k -= 1
        idx = sl.bisect_left(x + 1) - 1
        if idx >= k:
            print(sl[idx - k])
        else:
            print(-1)
    elif query[0] == 3:
        _, x, k = query
        k -= 1
        idx = sl.bisect_right(x - 1)
        if idx + k < len(sl):
            print(sl[idx + k])
        else:
            print(-1)
