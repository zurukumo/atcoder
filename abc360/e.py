N, K = map(int, input().split())

mod = 998244353
inv = pow(N, mod - 2, mod)

ret = 0
a = 1
b = 0
for _ in range(K):
    a = a * (N - 2) * inv + 2 * inv * inv
    b = b * (N - 2) * inv + 2 * inv * inv
    a %= mod
    b %= mod

ret = a + b * (2 + N) * (N - 1) // 2
print(ret % mod)
