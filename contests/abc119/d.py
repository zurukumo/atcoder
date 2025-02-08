import sys
from bisect import bisect_left

input = sys.stdin.readline

A, B, Q = map(int, input().split())

INF = 10**12
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]

ret = []
for _ in range(Q):
    x = int(input())
    spos = bisect_left(s, x)
    tpos = bisect_left(t, x)
    ls, rs = s[spos - 1], s[spos]
    lt, rt = t[tpos - 1], t[tpos]
    if ls < lt:
        if rs < rt:
            ret.append(min(x - ls, rt - x, min(x - lt, rs - x) + rs - lt))
        else:
            ret.append(min(x - ls, rs - x))
    else:
        if rs < rt:
            ret.append(min(x - lt, rt - x))
        else:
            ret.append(min(x - lt, rs - x, min(x - ls, rt - x) + rt - ls))

for r in ret:
    print(r)
