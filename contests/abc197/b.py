H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

X, Y = X - 1, Y - 1

ret = 0
for y in range(Y - 1, -1, -1):
    if S[X][y] == ".":
        ret += 1
    else:
        break

for y in range(Y + 1, W):
    if S[X][y] == ".":
        ret += 1
    else:
        break

for x in range(X - 1, -1, -1):
    if S[x][Y] == ".":
        ret += 1
    else:
        break

for x in range(X + 1, H):
    if S[x][Y] == ".":
        ret += 1
    else:
        break

if S[X][Y] == ".":
    ret += 1

print(ret)
