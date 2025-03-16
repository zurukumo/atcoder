N = int(input())
P = [int(i) for i in input().split()]

dp = [-float("inf")] * (N + 1)
dp[0] = 0
for p in P:
    for i in range(N, 0, -1):
        dp[i] = max(dp[i], dp[i - 1] * 0.9 + p)

ret = -float("inf")
for k in range(1, N + 1):
    ret = max(ret, dp[k] / (10 * (1 - (0.9) ** k)) - 1200 / k**0.5)

print(ret)
