import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, x = map(int, input().split())
h = [int(i) for i in input().split()]
v = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    v[a - 1].append(b - 1)
    v[b - 1].append(a - 1)


def rec(pre, cur):
    c = 0
    for nex in v[cur]:
        if nex == pre:
            continue
        c += rec(cur, nex)

    if h[cur] == 1 or c != 0:
        return c + 1
    else:
        return c


print(max(0, (rec(-1, x - 1) - 1) * 2))
