S = int(input())

mod = 10**9 + 7
dp = [0] * 2001
dp[0] = 1

for i in range(3, 2001):
    dp[i] = sum(dp[: i - 2]) % mod

print(dp[S])
