N, M = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

tree = 0
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    stack = [i]
    visited[i] = True
    while stack:
        cur = stack.pop()
        for nex in graph[cur]:
            if not visited[nex]:
                stack.append(nex)
                visited[nex] = True
    tree += 1

print(max(0, M - (N - tree)))
