N = int(input())

dp = [[0] * 6 for _ in range(N)]
for i in range(6):
    dp[0][i] = i + 1

for i in range(1, N):
    for j in range(6):
        dp[i][j] = max(j + 1, sum(dp[i - 1]) / 6)

print(sum(dp[N - 1]) / 6)
