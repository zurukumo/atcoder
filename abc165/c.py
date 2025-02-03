import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split())
abcd = [[int(i) for i in input().split()] for _ in range(Q)]

ret = -float("inf")


def dfs(A, cur, depth):
    if depth == N:
        s = 0
        for a, b, c, d in abcd:
            a, b = a - 1, b - 1
            if A[b] - A[a] == c:
                s += d
        global ret
        ret = max(ret, s)
        return

    for nex in range(cur, M + 1):
        dfs(A + [nex], nex, depth + 1)


dfs([], 1, 0)

print(ret)
