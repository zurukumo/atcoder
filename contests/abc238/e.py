N, Q = map(int, input().split())
lr = [[int(i) for i in input().split()] for _ in range(Q)]

graph = [[] for _ in range(N + 1)]
for l, r in lr:
    l -= 1
    r -= 1
    graph[l].append(r + 1)
    graph[r + 1].append(l)

stack = [0]
visited = [False] * (N + 1)
visited[0] = True
while stack:
    cur = stack.pop()
    for nex in graph[cur]:
        if not visited[nex]:
            visited[nex] = True
            stack.append(nex)

if visited[N]:
    print("Yes")
else:
    print("No")
