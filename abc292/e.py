N, M = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[] for _ in range(N)]
for u, v in uv:
    graph[u - 1].append(v - 1)

ret = 0
for i in range(N):
    queue = []
    visited = set()

    queue.append(i)
    visited.add(i)
    while queue:
        u = queue.pop()
        for v in graph[u]:
            if v not in visited:
                queue.append(v)
                visited.add(v)

    ret += len(visited) - 1

print(ret - M)
