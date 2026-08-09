import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

X1, X2, X3 = map(int, input().split())

mod = 998244353

fac = [1]
for i in range(1, X1 + X2 + X3 + 1):
    fac.append(fac[-1] * i % mod)
inv = [pow(fac[-1], mod - 2, mod)]
for i in range(X1 + X2 + X3, 0, -1):
    inv.append(inv[-1] * i % mod)
inv.reverse()


def comb(n, r):
    if r == 0:
        return 1
    return fac[n] * inv[n - r] * inv[r] % mod


ret = 0
for x1_group in range(1, X1 + 1):
    for x3_group in [x1_group - 1, x1_group, x1_group + 1]:
        if not 1 <= x3_group <= X3:
            continue

        rest_x2 = X2 - (x1_group + x3_group - 1)
        if rest_x2 < 0:
            continue

        s = (comb(X1 - 1, x1_group - 1) * comb(X3 - 1, x3_group - 1) * comb(X1 + X3 + rest_x2, rest_x2)) % mod
        if x1_group == x3_group:
            s *= 2
        ret += s
        ret %= mod

print(ret)
