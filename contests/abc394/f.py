import sys

sys.setrecursionlimit(10**7)

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N - 1)]

graph = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ret = -1


def dfs(cur, pre=-1):
    s = []
    for nex in graph[cur]:
        if nex == pre:
            continue
        s.append(dfs(nex, cur))

    s.sort(reverse=True)
    global ret
    if len(s) >= 4:
        ret = max(ret, sum(s[:4]) + 1)
    if len(s) >= 3:
        if pre != -1:
            ret = max(ret, sum(s[:3]) + 2)
        return sum(s[:3]) + 1
    return 1


dfs(0)

print(ret)
