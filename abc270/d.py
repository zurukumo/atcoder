import sys

sys.setrecursionlimit(10**5)

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

dp = [-1] * (N + 1)
dp[0] = 0


def dfs(n):
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    M = -float("inf")
    for a in A:
        if a > n:
            break
        M = max(M, n - dfs(n - a))

    dp[n] = M
    return M


print(dfs(N))
