import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(H)]

MOD = 10**9 + 7
D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

dp = [[-1] * W for _ in range(H)]


def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    s = 1
    for di, dj in D:
        i_, j_ = i + di, j + dj
        if 0 <= i_ < H and 0 <= j_ < W and a[i][j] < a[i_][j_]:
            s += dfs(i_, j_)
            s %= MOD

    dp[i][j] = s

    return s


ret = 0
for i in range(H):
    for j in range(W):
        ret += dfs(i, j)
        ret %= MOD

print(ret)
