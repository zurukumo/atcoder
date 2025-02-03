H, W, h, w = map(int, input().split())

if h == w == 1:
    print("No")

else:
    a = (10**9 - 1) // (h * w - 1)
    ret = [[a] * W for _ in range(H)]
    for y in range(h - 1, H, h):
        for x in range(w - 1, W, w):
            ret[y][x] = -a * (h * w - 1) - 1

    s = 0
    for y in range(H):
        s += sum(ret[y])

    if s > 0:
        print("Yes")
        for r in ret:
            print(*r)
    else:
        print("No")
