r1, c1, r2, c2 = map(int, input().split())
mod = 10**9 + 7

fac = [1]
for i in range(1, r2 + c2 + 10):
    fac.append(fac[-1] * i % mod)
inv = [pow(fac[-1], mod - 2, mod)]
for i in range(r2 + c2 + 9, 0, -1):
    inv.append(inv[-1] * i % mod)
inv = inv[::-1]


def comb(n, r):
    return fac[n] * inv[n - r] * inv[r] % mod


def g(x, y):
    return comb(x + y, y)


ret = g(r2 + 1, c2 + 1) - g(r2 + 1, c1) - g(r1, c2 + 1) + g(r1, c1)
ret %= mod

print(ret)
