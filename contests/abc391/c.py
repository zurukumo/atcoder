N, Q = map(int, input().split())

ret = 0
count = [1] * N
where = [i for i in range(N)]

for _ in range(Q):
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        _, p, h = query
        now = where[p - 1]
        if count[h - 1] == 1:
            ret += 1
        count[h - 1] += 1
        where[p - 1] = h - 1
        if count[now] == 2:
            ret -= 1
        count[now] -= 1
    else:
        print(ret)
