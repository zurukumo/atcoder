K = int(input())
C = [int(i) for i in input().split()]

mod = 998244353

fac = [1]
inv = [1]
for i in range(1, 1001):
    fac.append(fac[-1] * i % mod)
    inv.append(pow(fac[-1], mod - 2, mod))


dp = [0] * (K + 1)
dp[0] = 1
for j in range(26):
    ndp = [0] * (K + 1)
    for k in range(C[j] + 1):
        for i in range(K + 1):
            if i + k <= K:
                ndp[i + k] += dp[i] * inv[k]
                ndp[i + k] %= mod
    dp = ndp

ret = 0
for i in range(1, K + 1):
    ret += dp[i] * fac[i]
    ret %= mod

print(ret)
