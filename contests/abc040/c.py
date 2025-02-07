N = int(input())
a = [int(i) for i in input().split()]

dp = [float("inf")] * N
dp[0] = 0

for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], abs(a[i + 1] - a[i]) + dp[i])
    if i + 2 <= N - 1:
        dp[i + 2] = min(dp[i + 2], abs(a[i + 2] - a[i]) + dp[i])

print(dp[N - 1])
