N = int(input())

xyh1 = []  # h > 0
xyh2 = []  # h = 0
for _ in range(N):
    x, y, h = map(int, input().split())
    if h > 0:
        xyh1.append((x, y, h))
    else:
        xyh2.append((x, y, h))


def solve():
    for Cx in range(0, 101):
        for Cy in range(0, 101):
            # 特定できるからxyh1は必ず1つは要素を持つ
            x, y, h = xyh1[0]
            H = h + abs(x - Cx) + abs(y - Cy)

            flag = False
            for x, y, h in xyh1[1:]:
                if H != h + abs(x - Cx) + abs(y - Cy):
                    flag = True
                    break

            if flag:
                continue

            for x, y, h in xyh2:
                if H - abs(x - Cx) - abs(y - Cy) > 0:
                    flag = True
                    break

            if flag:
                continue

            return (Cx, Cy, H)


print(*solve())
