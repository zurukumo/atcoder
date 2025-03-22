H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dp = [[-1] * W for _ in range(H)]


def dfs(y, x):
    if not 0 <= y < H or not 0 <= x < W or S[y][x] == "#":
        return 0

    if dp[y][x] != -1:
        return dp[y][x]

    if dfs(y + 1, x) or dfs(y, x + 1) or dfs(y + 1, x + 1):
        dp[y][x] = 0
        return 0

    dp[y][x] = 1
    return 1


dfs(0, 0)

if dp[0][0] == 0:
    print("First")
else:
    print("Second")
