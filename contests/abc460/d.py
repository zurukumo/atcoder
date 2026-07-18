import collections
import itertools

H, W = map(int, input().split())
S = [input() for _ in range(H)]

T = [["=" for _ in range(W)] for _ in range(H)]

queue = collections.deque([])
for y in range(H):
    for x in range(W):
        if S[y][x] != "#":
            continue
        for dy, dx in itertools.product((-1, 0, 1), repeat=2):
            if dy == dx == 0:
                continue
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == ".":
                queue.append((y, x, "#"))
                T[y][x] = "#"
                break

while queue:
    y, x, c = queue.popleft()
    for dy, dx in itertools.product((-1, 0, 1), repeat=2):
        if dy == dx == 0:
            continue
        ny = y + dy
        nx = x + dx
        nc = "." if c == "#" else "#"
        if 0 <= ny < H and 0 <= nx < W and T[ny][nx] == "=":
            queue.append((ny, nx, nc))
            T[ny][nx] = nc

for t in T:
    print("".join(t).replace("=", "."))
