from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
K = [int(input()) for _ in range(Q)]

sa = set(A)
for k in K:
    ng, ok = 0, 10**19
    while ok - ng > 1:
        m = (ng + ok) // 2
        if m - bisect_left(A, m) >= k:
            ok = m
        else:
            ng = m

    while ok in sa:
        ok += 1
    print(ok)
    # print()
