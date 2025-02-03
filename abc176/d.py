H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
A = [[i for i in input()] for _ in range(H)]

visited = [[-1] * W for i in range(H)]
visited[Ch - 1][Cw - 1] = 0
h = [(Ch - 1, Cw - 1)]
c = 0
while True:
    done = []
    while h:
        cy, cx = h.pop()
        done.append((cy, cx))
        visited[cy][cx] = c
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if (
                0 <= ny < H
                and 0 <= nx < W
                and A[ny][nx] == "."
                and visited[ny][nx] == -1
            ):
                h.append((ny, nx))
                visited[ny][nx] = c

    h = []
    for cy, cx in done:
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                ny, nx = cy + dy, cx + dx
                if (
                    0 <= ny < H
                    and 0 <= nx < W
                    and A[ny][nx] == "."
                    and visited[ny][nx] == -1
                ):
                    h.append((ny, nx))
    if not h:
        break
    c += 1

print(visited[Dh - 1][Dw - 1])
