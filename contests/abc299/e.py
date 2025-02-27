import collections

N, M = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]
K = int(input())
pd = [[int(i) for i in input().split()] for _ in range(K)]

graph = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


colors = [1] * N

for p, d in pd:
    p -= 1
    queue = collections.deque()
    visited = [False] * N

    if 0 < d:
        queue.append((p, 0))
        visited[p] = True
        colors[p] = 0

    while queue:
        cur, dist = queue.popleft()
        for nex in graph[cur]:
            if not visited[nex] and dist + 1 < d:
                queue.append((nex, dist + 1))
                visited[nex] = True
                colors[nex] = 0

for p, d in pd:
    p -= 1
    queue = collections.deque()
    visited = [False] * N

    color = 0

    queue.append((p, 0))
    visited[p] = True
    if 0 == d:
        color |= colors[p]

    while queue:
        cur, dist = queue.popleft()
        for nex in graph[cur]:
            if not visited[nex]:
                if dist + 1 == d:
                    color |= colors[nex]
                else:
                    queue.append((nex, dist + 1))
                    visited[nex] = True

    if color == 0:
        print("No")
        exit()

print("Yes")
print("".join(str(c) for c in colors))
