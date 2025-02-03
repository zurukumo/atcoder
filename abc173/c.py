H, W, K = map(int, input().split())
c = [[i == "#" for i in input()] for _ in range(H)]

ret = 0
for x in range(1 << W):
    for y in range(1 << H):
        s = 0
        for i in range(W):
            for j in range(H):
                if x & (1 << i) or y & (1 << j):
                    continue
                s += c[j][i]
        if s == K:
            ret += 1

print(ret)
