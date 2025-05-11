A, B, C, D = map(int, input().split())


mod = 998244353

fac = [1]
for i in range(1, A + B + C + D + 1):
    fac.append(fac[-1] * i % mod)
inv = [pow(fac[-1], mod - 2, mod)]
for i in range(A + B + C + D, 0, -1):
    inv.append(inv[-1] * i % mod)
inv.reverse()


def choose(n, k):
    if n < k or k < 0:
        return 0
    return fac[n] * inv[k] % mod


ret = 0
for orange in range(B + 1):
    rest_orange = B - orange
    comb1 = fac[A - 1 + rest_orange] * inv[A - 1] * inv[rest_orange] % mod
    comb2 = fac[orange + C + D] * inv[orange + D] * inv[C] % mod
    ret += comb1 * comb2 % mod
    ret %= mod

print(ret)
