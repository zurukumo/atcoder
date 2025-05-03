N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

ret = float("inf")

rotatedS = [[""] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        rotatedS[i][j] = S[i][j]

for i in range(4):
    tmp = i
    for j in range(N):
        for k in range(N):
            if rotatedS[j][k] != T[j][k]:
                tmp += 1
    ret = min(ret, tmp)

    n_rotatedS = [[""] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            n_rotatedS[j][k] = rotatedS[N - k - 1][j]
    rotatedS = n_rotatedS

print(ret)
