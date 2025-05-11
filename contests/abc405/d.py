import collections

H, W = map(int, input().split())
S = [input() for _ in range(H)]

T = [[""] * W for _ in range(H)]
queue = collections.deque()
visisted = [[False] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x] == "E":
            queue.append((y, x))
            visisted[y][x] = True
            T[y][x] = "E"
        elif S[y][x] == "#":
            T[y][x] = "#"

while queue:
    y, x = queue.popleft()
    for di, (dy, dx) in enumerate(((-1, 0), (1, 0), (0, -1), (0, 1))):
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and not visisted[ny][nx] and S[ny][nx] != "#":
            queue.append((ny, nx))
            visisted[ny][nx] = True
            if di == 0:
                T[ny][nx] = "v"
            elif di == 1:
                T[ny][nx] = "^"
            elif di == 2:
                T[ny][nx] = ">"
            elif di == 3:
                T[ny][nx] = "<"

for row in T:
    print("".join(row))
