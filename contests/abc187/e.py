import collections
import sys

sys.setrecursionlimit(10**7)

N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N - 1)]
Q = int(input())
tex = [[int(i) for i in input().split()] for _ in range(Q)]


graph = [[] for _ in range(N)]
for i, (a, b) in enumerate(ab):
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

cost = collections.defaultdict(int)
for t, e, x in tex:
    a, b = ab[e - 1]
    if t == 1:
        a, b = b, a
    cost[(a - 1, b - 1)] += x

ans = [0] * N


def dfs(pre, cur):
    s = 0
    for nex in graph[cur]:
        if nex == pre:
            continue
        s += dfs(cur, nex) + cost[(nex, cur)]
    ans[cur] = s
    return s


dfs(-1, 0)

queue = [0]
visited = [False] * N
visited[0] = True
while queue:
    cur = queue.pop()
    for nex in graph[cur]:
        if visited[nex]:
            continue
        ans[nex] += ans[cur] - ans[nex] + cost[(cur, nex)] - cost[(nex, cur)]
        queue.append(nex)
        visited[nex] = True

for row in ans:
    print(row)
