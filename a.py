N, M = map(int, input().split())
vec = [[float('inf')] * N for _ in range(N)]
for _ in range(M) :
    A, B, C = map(int, input().split())
    vec[A-1][B-1] = C
    vec[B-1][A-1] = C

for i in range(N) :
    vec[i][i] = 0

# ワーシャルフロイド
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            vec[i][j] = min(vec[i][j], vec[i][k] + vec[k][j])

for i in range(N) :
    print(vec[i])

K = int(input())
for _ in range(K) :
    X, Y, Z = map(int, input().split())

