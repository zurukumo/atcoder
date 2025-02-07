import heapq

Q = int(input())
Query = [input() for _ in range(Q)]

ans = 0

lq = []
rq = []

for q in Query:
    if q[0] == "1":
        a, b = map(int, q[2:].split())

        heapq.heappush(lq, -a)
        heapq.heappush(rq, a)

        lmax, rmin = -lq[0], rq[0]
        if lmax > rmin:
            lmax, rmin = rmin, lmax
            ans += rmin - lmax

            heapq.heappop(lq)
            heapq.heappop(rq)
            heapq.heappush(lq, -lmax)
            heapq.heappush(rq, rmin)

        ans += b

    else:
        print(-lq[0], ans)
