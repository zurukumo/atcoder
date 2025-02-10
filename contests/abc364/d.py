import bisect

N, Q = map(int, input().split())
a = [int(i) for i in input().split()]
bk = [[int(i) for i in input().split()] for _ in range(Q)]

a.append(-float("inf"))
a.append(float("inf"))
a.sort()


for b, k in bk:
    ng = -1
    ok = 10**10
    while ok - ng > 1:
        mid = (ng + ok) // 2
        l = bisect.bisect_left(a, b - mid)
        r = bisect.bisect_right(a, b + mid) - 1
        if r - l + 1 >= k:
            ok = mid
        else:
            ng = mid
    print(ok)
