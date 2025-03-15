import sys

sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(N * K - 1)]

graph = [[] for _ in range(N * K)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(cur, pre):
    mem = []
    for nex in graph[cur]:
        if nex == pre:
            continue
        x = dfs(nex, cur)
        if x % K != 0:
            mem.append(x)

    if len(mem) == 0:
        return 1
    if len(mem) == 1:
        return mem[0] + 1
    if len(mem) == 2 and sum(mem) + 1 == K:
        return 0

    print("No")
    exit()


dfs(0, -1)

print("Yes")
