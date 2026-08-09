import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


M, A, B = map(int, input().split())

ok = dict()
visited = set()


def dfs(pp, p):
    if (pp, p) in ok:
        return ok[(pp, p)]

    visited.add((pp, p))

    c = (A * p + B * pp) % M
    if c == 0:
        ok[(p, c)] = False
        return False

    if (p, c) in visited:
        ok[(p, c)] = True
        return True

    ok[(pp, p)] = dfs(p, c)
    return ok[(pp, p)]


ret = 0
for i in range(1, M):
    for j in range(1, M):
        visited = set()
        if dfs(i, j):
            ret += 1
print(ret)
