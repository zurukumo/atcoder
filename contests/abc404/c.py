import collections

N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

cnt = collections.defaultdict(int)
graph = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1
    graph[a].append(b)
    graph[b].append(a)

if not all(cnt[i] == 2 for i in range(N)):
    print("No")
    exit()

stack = [0]
visited = [False] * N
visited[0] = True
while stack:
    v = stack.pop()
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            stack.append(u)

if all(visited):
    print("Yes")
else:
    print("No")
