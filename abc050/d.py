N = int(input())
MOD = 10**9 + 7

M = len(bin(N)) - 2
dp = [[0] * 3 for _ in range(M + 1)]
dp[0][0] = 1

for i in range(M):
    if N >> (M - i - 1) & 1:
        dp[i + 1][0] = dp[i][0] % MOD
        dp[i + 1][1] = (dp[i][0] + dp[i][1]) % MOD
        dp[i + 1][2] = (dp[i][1] * 2 + dp[i][2] * 3) % MOD
    else:
        dp[i + 1][0] = (dp[i][0] + dp[i][1]) % MOD
        dp[i + 1][1] = dp[i][1] % MOD
        dp[i + 1][2] = (dp[i][1] + dp[i][2] * 3) % MOD

print(sum(dp[-1]) % MOD)
