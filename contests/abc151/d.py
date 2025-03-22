import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
S = [input() for _ in range(H)]

ret = 0
for sy in range(H):
    for sx in range(W):
        if S[sy][sx] == "#":
            continue

        cost = [[float("inf")] * W for _ in range(H)]
        cost[sy][sx] = 0

        q = deque([(sy, sx, 0)])
        while q:
            cy, cx, co = q.popleft()
            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < H and 0 <= nx < W and S[ny][nx] != "#" and co + 1 < cost[ny][nx]:
                    q.append((ny, nx, co + 1))
                    cost[ny][nx] = co + 1
                    ret = max(ret, co + 1)

print(ret)
