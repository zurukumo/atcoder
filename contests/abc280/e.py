N, P = map(int, input().split())

mod = 998244353
inv = pow(100, mod - 2, mod)

dp = [0] * N
dp[0] = 0

for i in range(N):
    if i + 2 < N:
        dp[i + 2] += (dp[i] + 1) * P * inv
        dp[i + 2] %= mod
    if i + 1 < N:
        dp[i + 1] += (dp[i] + 1) * (100 - P) * inv
        dp[i + 1] %= mod

print((dp[-1] + 1) % mod)
