import sortedcontainers

N, Q = map(int, input().split())


sl = sortedcontainers.SortedList(range(N))
mem = dict()
for i in range(N):
    mem[i] = (i, 1, i)


colors = [1] * N

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1:]
        x -= 1
        c -= 1
        idx = sl.bisect_left(x + 1) - 1
        cleft, ccount, ccolor = mem[sl[idx]]
        colors[ccolor] -= ccount
        colors[c] += ccount
        mem[sl[idx]] = (cleft, ccount, c)
        if idx + 1 < len(sl):
            nleft, ncount, ncolor = mem[sl[idx + 1]]
            if c == ncolor:
                mem[sl[idx]] = (cleft, ccount + ncount, c)
                ccount += ncount
                sl.pop(idx + 1)
        if idx - 1 >= 0:
            pleft, pcount, pcolor = mem[sl[idx - 1]]
            if c == pcolor:
                mem[sl[idx - 1]] = (pleft, pcount + ccount, c)
                sl.pop(idx)

    else:
        c = query[1]
        c -= 1
        print(colors[c])
