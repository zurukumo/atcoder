import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]


vec = [[] for _ in range(N + 1)]
for i, (x, y) in enumerate(xy):
    vec[x].append((i + 1, y))

ret = []


def dfs(curs):
    curs.sort()
    ret.extend(curs)
    nex_kv = collections.defaultdict(list)
    for cur in curs:
        for nex, nval in vec[cur]:
            nex_kv[nval].append(nex)

    keys = sorted(nex_kv.keys())
    for key in keys:
        nexs = nex_kv[key]
        dfs(nexs.copy())


dfs([0])

print(*ret[1:])
