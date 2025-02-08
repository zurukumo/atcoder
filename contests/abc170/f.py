import sys
from heapq import heappop, heappush

input = sys.stdin.readline

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
c = [[i == "." for i in input()] for _ in range(H)]

x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
INF = 1 << 60
dist = [INF] * (H * W * 2)


def pos(x, y, m):
    return (x * W + y) * 2 + m


dist[pos(x1, y1, 0)] = dist[pos(x1, y1, 1)] = 0

q = [(0, pos(x1, y1, 0)), (0, pos(x1, y1, 1))]
while q:
    ccost, cpos = heappop(q)
    if ccost > dist[cpos]:
        continue
    cx = cpos // 2 // W
    cy = cpos // 2 % W
    cmode = cpos % 2
    dir = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
    for dx, dy in dir[cmode]:
        nx, ny = cx + dx, cy + dy
        ncost = ccost + 1
        if (
            0 <= nx < H
            and 0 <= ny < W
            and c[nx][ny]
            and ncost < dist[pos(nx, ny, cmode)]
        ):
            heappush(q, (ncost, pos(nx, ny, cmode)))
            dist[pos(nx, ny, cmode)] = ncost

    ncost = (ccost + K - 1) // K * K
    if ncost < dist[pos(cx, cy, cmode ^ 1)]:
        dist[pos(cx, cy, cmode ^ 1)] = ncost
        heappush(q, (ncost, pos(cx, cy, cmode ^ 1)))

ans = min(dist[pos(x2, y2, 0)], dist[pos(x2, y2, 1)])
if ans == INF:
    print(-1)
else:
    print((ans + K - 1) // K)
