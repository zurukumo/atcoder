from bisect import bisect_right
from collections import defaultdict

all, N, M = map(int, input().split())
L = [int(input()) for _ in range(N)]
xy = [[int(i) for i in input().split()] for _ in range(M)]

cnt = defaultdict(lambda: [0, 0])
cnt[0] = [0, 0]
for i in range(1, N):
    s = L[i] - L[i - 1] - 1
    cnt[s][0] += s
    cnt[s][1] += 1

item = sorted(cnt.items())
key = [item[i][0] for i in range(len(item))]
val = [list(item[i][1]) for i in range(len(item))]

for i in range(1, len(item)):
    val[i][0] += val[i - 1][0]
    val[i][1] += val[i - 1][1]

for x, y in xy:
    i = bisect_right(key, x + y) - 1
    ret = N + val[i][0] + (N - val[i][1] - 1) * (x + y)
    ret += min(L[0] - 1, x)
    ret += min(all - L[-1], y)
    print(ret)
