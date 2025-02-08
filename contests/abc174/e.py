from math import ceil, floor

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

ng, ok = 0, 10**9
for _ in range(50):
    mid = (ng + ok) / 2
    ret = 0
    for a in A:
        ret += floor(a / mid)
    if ret <= K:
        ok = mid
    else:
        ng = mid

print(ceil(ng))
