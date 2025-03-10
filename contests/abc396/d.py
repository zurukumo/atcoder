N, M = map(int, input().split())
uvw = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[float("inf")] * N for _ in range(N)]
for u, v, w in uvw:
    u -= 1
    v -= 1
    graph[u][v] = w
    graph[v][u] = w

ret = float("inf")


def dfs(path, cur, s):
    global ret
    if cur == N - 1:
        ret = min(ret, s)
        return

    for nex in range(N):
        if nex == cur or graph[cur][nex] == float("inf") or nex in path:
            continue
        path.add(nex)
        dfs(path, nex, s ^ graph[cur][nex])
        path.remove(nex)


dfs(set([0]), 0, 0)

print(ret)
