import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
xytr = [list(map(int, input().split())) for _ in range(N)]

cost = [float("inf")] * N
cost[0] = 0

hp = [(0, 0)]
while hp:
    cco, cur = heappop(hp)
    if cost[cur] < cco:
        continue
    for nex in range(N):
        if cur == nex:
            continue
        xi, yi, ti, ri = xytr[cur]
        xj, yj, tj, rj = xytr[nex]
        diff = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
        nco = diff / min(ti, rj)
        if cco + nco < cost[nex]:
            cost[nex] = cco + nco
            heappush(hp, (cost[nex], nex))

cost.sort(reverse=True)

ret = 0
for i in range(N - 1):
    ret = max(ret, cost[i] + i)
print(ret)
