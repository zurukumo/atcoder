r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def judge():
    if r1 == r2 and c1 == c2:
        return 0

    if abs(r2 - r1) == abs(c2 - c1):
        return 1

    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) > 3:
                continue

            if r1 == r2 + i and c1 == c2 + j:
                return 1

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2

    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) > 3:
                continue

            if abs((r2 + i) - r1) == abs((c2 + j) - c1):
                return 2

            for k in range(-3, 4):
                for l in range(-3, 4):
                    if r1 == r2 + i + k and c1 == c2 + j + l:
                        return 2

    return 3


print(judge())
