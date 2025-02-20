N, M, K = map(int, input().split())


mod = 998244353

dp = [0] * (K + 1)
dp[0] = 1
for _ in range(N):
    ndp = [0] * (K + 1)
    for i in range(K, -1, -1):
        for j in range(1, M + 1):
            if i - j >= 0:
                ndp[i] += dp[i - j]
                ndp[i] %= mod
    dp = ndp

print(sum(dp) % mod)
