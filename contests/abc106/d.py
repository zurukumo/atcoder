from bisect import bisect_left
import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    L, R = map(int, input().split())
    dp[L][R] += 1

for i in range(N + 1):
    for j in range(N + 1):
        if 0 <= i - 1:
            dp[i][j] += dp[i - 1][j]
        if 0 <= j - 1:
            dp[i][j] += dp[i][j - 1]
        if 0 <= i - 1 and 0 <= j - 1:
            dp[i][j] -= dp[i - 1][j - 1]

for _ in range(Q):
    p, q = map(int, input().split())
    print(dp[q][q] - dp[p - 1][q] - dp[q][p - 1] + dp[p - 1][p - 1])
