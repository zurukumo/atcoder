n, a, b = map(int, input().split())

mod = 10**9 + 7

ret = pow(2, n, mod) - 1


def comb(n, r):
    ret = 1
    for i in range(n - r + 1, n + 1):
        ret *= i
        ret %= mod
    for i in range(1, r + 1):
        ret *= pow(i, mod - 2, mod)
        ret %= mod
    return ret


ret -= comb(n, a)
ret -= comb(n, b)

print(ret % mod)
