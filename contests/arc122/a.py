import sys

sys.setrecursionlimit(10**6)

N = int(input())
A = [int(i) for i in input().split()]

mod = 10**9 + 7

ret = 0


def dfs(i, p, n):
    if i == N - 1:
        p2, n2 = p, n
    else:
        p2, n2 = dfs(i + 1, (p + n) % mod, p)
        inv = pow(p + n, mod - 2, mod)
        p2, n2 = p2 * p * inv + n2, p2 * n * inv

    global ret
    ret += A[i] * (p2 - n2) % mod
    ret %= mod

    return p2 % mod, n2 % mod


dfs(0, 1, 0)

print(ret)
