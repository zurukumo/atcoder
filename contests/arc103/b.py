N = int(input())
XY = [[int(i) for i in input().split()] for _ in range(N)]

if len(set([(X + Y) % 2 for X, Y in XY])) != 1:
    print(-1)

else:
    d = []
    for i in range(32, -1, -1):
        d.append(1 << i)

    if (XY[0][0] + XY[0][1]) % 2 == 0:
        d.append(1)

    print(len(d))
    print(*d)

    for X, Y in XY:
        ret = ""
        cx, cy = 0, 0
        for i in range(len(d)):
            mj, mv = 0, float("inf")
            diff = [(d[i], 0), (-d[i], 0), (0, d[i]), (0, -d[i])]
            for j, (dx, dy) in enumerate(diff):
                if (cx + dx - X) ** 2 + (cy + dy - Y) ** 2 < mv:
                    mj = j
                    mv = (cx + dx - X) ** 2 + (cy + dy - Y) ** 2

            if mj == 0:
                ret += "R"
                cx += d[i]
            elif mj == 1:
                ret += "L"
                cx -= d[i]
            elif mj == 2:
                ret += "U"
                cy += d[i]
            else:
                ret += "D"
                cy -= d[i]

        print(ret)
