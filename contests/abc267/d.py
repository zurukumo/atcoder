N, M = map(int, input().split())
A = [int(i) for i in input().split()]

dp = [[-float("inf")] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N + 1):
    for j in range(M + 1):
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + A[i - 1] * j)
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(dp[N][M])
