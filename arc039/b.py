N, K = map(int, input().split())
mod = 10**9 + 7

fac = [1]
inv = [1]
for i in range(1, N + K):
    fac.append(fac[-1] * i % mod)
    inv.append(pow(fac[-1], mod - 2, mod))

if K < N:
    print(fac[N + K - 1] * inv[N - 1] * inv[K] % mod)

else:
    K %= N
    print(fac[N] * inv[N - K] * inv[K] % mod)
