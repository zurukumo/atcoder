import sys

sys.setrecursionlimit(10**7)

T = int(input())


def dfs(S, H, W, y, x):
    flag = False
    for dy in [0, 1]:
        for dx in [0, 1]:
            if 0 <= y + dy < H and 0 <= x + dx < W and S[y + dy][x + dx] == ".":
                flag = True

    if flag:
        if y == H - 2 and x == W - 2:
            return 0
        elif x == W - 2:
            return dfs(S, H, W, y + 1, 0)
        else:
            return dfs(S, H, W, y, x + 1)

    else:
        m = float("inf")
        for dx in [0, 1]:
            S[y + 1][x + dx] = "."
            m = min(m, dfs(S, H, W, y, x) + 1)
            S[y + 1][x + dx] = "#"
        return m


for _ in range(T):
    H, W = map(int, input().split())
    S = [[c for c in input()] for _ in range(H)]

    print(dfs(S, H, W, 0, 0))
