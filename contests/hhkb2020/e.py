H, W = map(int, input().split())
S = [input() for _ in range(H)]

mod = 1000000007

s = [[0] * W for _ in range(H)]

k = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            k += 1

for x in range(W):
    light = 0
    for y in range(H):
        if S[y][x] == "#":
            light = 0
        else:
            s[y][x] += light
            light += 1

for x in range(W):
    light = 0
    for y in range(H - 1, -1, -1):
        if S[y][x] == "#":
            light = 0
        else:
            s[y][x] += light
            light += 1

for y in range(H):
    light = 0
    for x in range(W):
        if S[y][x] == "#":
            light = 0
        else:
            s[y][x] += light
            light += 1

for y in range(H):
    light = 0
    for x in range(W - 1, -1, -1):
        if S[y][x] == "#":
            light = 0
        else:
            s[y][x] += light
            light += 1

ret = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            continue
        ret += pow(2, k, mod) - pow(2, k - s[y][x] - 1, mod)
        ret %= mod

print(ret)
