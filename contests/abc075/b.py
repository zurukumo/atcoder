H, W = map(int, input().split())
S = [input() for _ in range(H)]

ret = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            for yy in range(max(0, y - 1), min(H, y + 2)):
                for xx in range(max(0, x - 1), min(W, x + 2)):
                    if S[yy][xx] != "#":
                        ret[yy][xx] += 1
                    else:
                        ret[yy][xx] = "#"
for i in range(H):
    s = "".join(map(str, ret[i]))
    print(s)
