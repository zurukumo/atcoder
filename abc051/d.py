N, M = map(int, input().split())

INF = float("inf")

vec1 = [[INF] * N for _ in range(N)]
vec2 = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    vec1[a - 1][b - 1] = vec1[b - 1][a - 1] = vec2[a - 1][b - 1] = vec2[b - 1][
        a - 1
    ] = c

for i in range(N):
    vec1[i][i] = vec2[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            vec1[i][j] = min(vec1[i][j], vec1[i][k] + vec1[k][j])

ret = 0
for i in range(N):
    for j in range(i + 1, N):
        if vec2[i][j] != INF and vec1[i][j] != vec2[i][j]:
            ret += 1

print(ret)
