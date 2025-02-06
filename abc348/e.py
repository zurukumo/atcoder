import sys

sys.setrecursionlimit(10**7)

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
C = [int(i) for i in input().split()]

graph = [[] for _ in range(N)]
for a, b in AB:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

slist = [0] * N
alist = [0] * N


def dfs(pre, cur):
    s = 0
    a = C[cur]
    for nex in graph[cur]:
        if nex == pre:
            continue
        ns, na = dfs(cur, nex)
        s += ns
        a += na
    slist[cur] = s
    alist[cur] = a
    return s + a, a


dfs(-1, 0)

queue = [(0, 0, 0)]
visited = [False] * N
visited[0] = True
while queue:
    cur, s, a = queue.pop()
    for nex in graph[cur]:
        if visited[nex]:
            continue
        cs = slist[cur] - slist[nex] - alist[nex]
        ca = alist[cur] - alist[nex]

        slist[nex] += cs + ca
        alist[nex] += ca
        queue.append((nex, cs + ca, ca + C[cur]))
        visited[nex] = True


print(min(slist))
