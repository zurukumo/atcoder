H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [["."] * W for _ in range(H)]
U = [["."] * W for _ in range(H)]

D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(H):
    for j in range(W):
        for di, dj in D:
            i_, j_ = i + di, j + dj
            if 0 <= i_ < H and 0 <= j_ < W:
                if S[i_][j_] == ".":
                    break
        else:
            T[i][j] = "#"

for i in range(H):
    for j in range(W):
        if T[i][j] == "#":
            for di, dj in D:
                i_, j_ = i + di, j + dj
                if 0 <= i_ < H and 0 <= j_ < W:
                    U[i_][j_] = "#"

flag = True
for i in range(H):
    for j in range(W):
        if S[i][j] != U[i][j]:
            flag = False
            break
    if not flag:
        break

if flag:
    print("possible")
    for t in T:
        print("".join(t))
else:
    print("impossible")
