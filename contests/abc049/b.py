H, W = map(int, input().split())
C = [[i for i in input()] for _ in range(H)]

C2 = [[""] * W for i in range(H * 2)]

for i in range(H):
    for j in range(W):
        i2 = i * 2
        C2[i2][j] = C2[i2 + 1][j] = C[i][j]

for i in range(H * 2):
    print("".join(C2[i]))
