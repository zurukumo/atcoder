N = int(input())
A = [int(i) for i in input().split()]

dp = [[[float("inf")] * 2 for _ in range(2)] for _ in range(N)]

dp[0][0][0] = 0
dp[0][1][1] = A[0]
for i in range(1, N):
    for j in range(2):
        dp[i][0][j] = min(dp[i][0][j], dp[i - 1][1][j])
        dp[i][1][j] = min(dp[i][1][j], dp[i - 1][0][j] + A[i], dp[i - 1][1][j] + A[i])

ret = min(dp[N - 1][0][1], dp[N - 1][1][0], dp[N - 1][1][1])

print(ret)
