H, W = map(int, input().split())
S = [[1 if i == "#" else 0 for i in input()] for _ in range(H)]

Hdp = [[0] * W for _ in range(H)]
Wdp = [[0] * W for _ in range(H)]

for i in range(H):
    start = 0
    count = 0
    for j in range(W):
        if S[i][j] == 1:
            for k in range(start, j):
                Hdp[i][k] = count
            start = j + 1
            count = 0
        else:
            count += 1

    for k in range(start, j + 1):
        Hdp[i][k] = count

for i in range(W):
    start = 0
    count = 0
    for j in range(H):
        if S[j][i] == 1:
            for k in range(start, j):
                Wdp[k][i] = count
            start = j + 1
            count = 0
        else:
            count += 1

    for k in range(start, j + 1):
        Wdp[k][i] = count

ret = 0
for i in range(H):
    for j in range(W):
        ret = max(ret, Hdp[i][j] + Wdp[i][j])

print(ret - 1)
