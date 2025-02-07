N, M, K = map(int, input().split())

mod = 998244353

fac = [1]
inv = [1]
for i in range(1, N + 10):
    fac.append(fac[-1] * i % mod)
    inv.append(pow(fac[-1], mod - 2, mod))


def comb(n, r):
    return fac[n] * inv[n - r] * inv[r] % mod


ret = 0
for k in range(K + 1):
    ret += comb(N - 1, k) * M * pow(M - 1, N - k - 1, mod) % mod
    ret %= mod
print(ret)
