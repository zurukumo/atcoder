import collections

H, W = map(int, input().split())
S = [input() for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1
B -= 1
C -= 1
D -= 1

cost = [[-1] * W for _ in range(H)]
cost[A][B] = 0
queue = collections.deque([(A, B, 0)])
while queue:
    y, x, c = queue.popleft()
    # 普通の移動
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "." and cost[ny][nx] == -1:
            cost[ny][nx] = c
            queue.appendleft((ny, nx, c))
    # ぶち破り1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "#" and cost[ny][nx] == -1:
            cost[ny][nx] = c + 1
            queue.append((ny, nx, c + 1))
    # ぶち破り2
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + 2 * dy, x + 2 * dx
        if 0 <= ny < H and 0 <= nx < W and (S[y + dy][x + dx] == "#" and S[ny][nx] == "#") and cost[ny][nx] == -1:
            cost[ny][nx] = c + 1
            queue.append((ny, nx, c + 1))


print(cost[C][D])
