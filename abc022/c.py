from itertools import combinations

N, M = map(int, input().split())
INF = 10 ** 10

vec = [[INF] * N for _ in range(N)]
for i in range(N) :
    vec[i][i] = 0

for _ in range(M) :
    u, v, l = map(int, input().split())
    vec[u-1][v-1] = vec[v-1][u-1] = l

for k in range(1, N) :
    for i in range(1, N) :
        for j in range(1, N) :
            vec[i][j] = min(vec[i][j], vec[i][k] + vec[k][j])

v0 = []
for i in range(1, N) :
    if vec[0][i] != INF :
        v0.append(i)

ret = INF
for i, j in combinations(v0, 2) :
    ret = min(ret, vec[0][i] + vec[i][j] + vec[j][0])

if ret == INF :
    print(-1)
else :
    print(ret)