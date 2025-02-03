N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

graph = [[] for _ in range(N)]
for a, b in zip(A, B):
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False] * N
bit = [0] * N

for start in range(N):
    if visited[start]:
        continue
    queue = [(start, 0)]
    visited[start] = True
    while queue:
        v, b = queue.pop()
        for u in graph[v]:
            if visited[u]:
                continue
            visited[u] = True
            bit[u] = b ^ 1
            queue.append((u, b ^ 1))

for i in range(N):
    for j in graph[i]:
        if bit[i] == bit[j]:
            print("No")
            exit()

print("Yes")
