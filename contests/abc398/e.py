N = int(input())
UV = [[int(i) for i in input().split()] for _ in range(N - 1)]

done = set()
vec = [[float("inf")] * N for _ in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    done.add((u, v))
    done.add((v, u))
    vec[u][v] = 1
    vec[v][u] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            vec[i][j] = min(vec[i][j], vec[i][k] + vec[k][j])

can_go = set()
for i in range(N):
    for j in range(i + 1, N):
        if vec[i][j] % 2 == 1 and (i, j) not in done:
            can_go.add((i, j))

if len(can_go) % 2 == 0:
    print("Second")
else:
    print("First")
    i, j = can_go.pop()
    print(i + 1, j + 1)

while can_go:
    i, j = map(int, input().split())
    can_go.remove((i - 1, j - 1))
    i, j = can_go.pop()
    print(i + 1, j + 1)
