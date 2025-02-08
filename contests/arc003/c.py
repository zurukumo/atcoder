from heapq import heappop, heappush

N, M = map(int, input().split())
c = [[i for i in input()] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if c[y][x] == "s":
            sy, sx = y, x
        if c[y][x] == "g":
            gy, gx = y, x


def solve():
    q = [(-float("inf"), gy, gx)]
    visited = [[False] * M for _ in range(N)]
    visited[gy][gx] = True

    while q:
        cost, cy, cx = heappop(q)
        cost *= -1

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M and c[ny][nx] != "#" and not visited[ny][nx]:
                visited[ny][nx] = True
                if c[ny][nx] == "s":
                    return cost * 0.99
                else:
                    heappush(q, (-min(cost * 0.99, int(c[ny][nx])), ny, nx))

    return -1


print(solve())
