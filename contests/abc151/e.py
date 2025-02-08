import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


N, K = map(int, input().split())
A = [int(i) for i in input().split()]
mod = 10**9 + 7

A.sort()

fac = [1]
inv = [1]
for i in range(1, N + 1):
    fac.append(fac[-1] * i % mod)
    inv.append(pow(fac[-1], mod - 2, mod))


def nCr(n, r):
    if r < 0 or n < r:
        return 0

    return fac[n] * inv[n - r] * inv[r] % mod


ret = 0
for i in range(N):
    l = N - i - 1
    u = i
    ret += A[i] * (nCr(u, K - 1) - nCr(l, K - 1))
    ret %= mod

print(ret)
