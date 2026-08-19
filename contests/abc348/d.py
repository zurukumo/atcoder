import heapq

H, W = map(int, input().split())
A = [input() for _ in range(H)]
N = int(input())
RCE = [[int(i) for i in input().split()] for _ in range(N)]


def solve():
    sx, sy = 0, 0
    gx, gy = 0, 0
    for y in range(H):
        for x in range(W):
            if A[y][x] == "S":
                sx, sy = x, y
            if A[y][x] == "T":
                gx, gy = x, y

    medicines = [[0] * W for _ in range(H)]
    for r, c, e in RCE:
        medicines[r - 1][c - 1] = e

    mem = [[0] * W for _ in range(H)]
    queue = [(-medicines[sy][sx], sy, sx)]
    mem[sy][sx] = medicines[sy][sx]
    while queue:
        ce, cy, cx = heapq.heappop(queue)
        ce *= -1

        if ce < mem[cy][cx] or ce == 0:
            continue

        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny = cy + dy
            nx = cx + dx

            if 0 <= ny < H and 0 <= nx < W and A[ny][nx] != "#":
                if (ny, nx) == (gy, gx):
                    return True

                ne = max(ce - 1, medicines[ny][nx])
                if ne > mem[ny][nx]:
                    heapq.heappush(queue, (-ne, ny, nx))
                    mem[ny][nx] = ne

    return False


if solve():
    print("Yes")
else:
    print("No")
