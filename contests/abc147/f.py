from collections import defaultdict
from heapq import heappop, heappush

N, X, D = map(int, input().split())

if D == 0:
    if X == 0:
        print(1)
    else:
        print(N + 1)

else:
    s = X * N + D * N * (N - 1) // 2

    h = defaultdict(lambda: [])
    for i in range(N + 1):
        a = X * i + D * i * (i - 1) // 2
        b = X * i + D * i * (2 * N - i - 1) // 2

        m = 2 * a - s
        M = 2 * b - s

        if M < m:
            m, M = M, m

        heappush(h[m % (abs(D) * 2)], (m, M))

    D = abs(D)

    ret = 0
    for heap in h.values():
        u, v = heappop(heap)
        while heap:
            if heap[0][0] <= v:
                v = max(v, heap[0][1])
                heappop(heap)
            else:
                ret += (v - u) // (2 * D) + 1
                u, v = heappop(heap)

        ret += (v - u) // (2 * D) + 1

    print(ret)
