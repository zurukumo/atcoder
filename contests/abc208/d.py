N, M = map(int, input().split())
ABC = [[int(i) for i in input().split()] for _ in range(M)]

ABC.sort(key=lambda x: max(x[0], x[1]))

vec = [[float("inf")] * N for _ in range(N)]
for A, B, C in ABC:
    vec[A - 1][B - 1] = C

ret = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            vec[i][j] = min(vec[i][j], vec[i][k] + vec[k][j])
    for i in range(N):
        for j in range(N):
            if i != j and vec[i][j] != float("inf"):
                ret += vec[i][j]


print(ret)
