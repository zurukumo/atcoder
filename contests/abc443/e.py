import collections

T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    S = [input() for _ in range(N)]

    breakable = [True] * N
    reached = [False] * N
    has_wall = [False] * N
    last_y = N

    queue = collections.deque([(N - 1, C - 1)])
    visited = set()
    reached[C - 1] = True
    while queue:
        y, x = queue.popleft()
        if y < last_y:
            for i in range(N):
                if S[y][i] == "#":
                    has_wall[i] = True
            for i in range(N):
                if not reached[i] and has_wall[i]:
                    breakable[i] = False
            last_y = y

        if y == 0:
            continue
        for dx in (-1, 0, 1):
            nx = x + dx
            if 0 <= nx < N and (breakable[nx] or S[y - 1][nx] == ".") and (y - 1, nx) not in visited:
                queue.append((y - 1, nx))
                visited.add((y - 1, nx))
                reached[nx] = True

    ret = ""
    for i in range(N):
        if (0, i) in visited:
            ret += "1"
        else:
            ret += "0"

    print(ret)
