N, M = map(int, input().split())
graph = [[float("inf")] * N for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1][B - 1] = graph[B - 1][A - 1] = 1

for i in range(N):
    graph[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    print(graph[i].count(2))
