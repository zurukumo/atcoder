import sys

sys.setrecursionlimit(10**7)

N, A, X, Y = map(int, input().split())

mem = dict()


def dfs(n):
    if n == 0:
        return 0
    if n in mem:
        return mem[n]

    a = X + dfs(n // A)
    b = (Y * 6 + dfs(n // 2) + dfs(n // 3) + dfs(n // 4) + dfs(n // 5) + dfs(n // 6)) / 5

    mem[n] = min(a, b)
    return mem[n]


print(dfs(N))
