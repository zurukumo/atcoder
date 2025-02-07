N, M, K = map(int, input().split())

mod = 998244353
inv = pow(M, mod - 2, mod)

dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1

for i in range(K + 1):
    for j in range(N):
        for k in range(1, M + 1):
            if i + 1 > K:
                continue
            if j + k <= N:
                dp[i + 1][j + k] += dp[i][j] * inv % mod
            else:
                dp[i + 1][N - (j + k - N)] += dp[i][j] * inv % mod

ret = 0
for i in range(K + 1):
    ret += dp[i][N]
    ret %= mod

print(ret)
