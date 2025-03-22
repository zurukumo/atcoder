import itertools

P = [[1 if i == "#" else 0 for i in input()] for _ in range(12)]

P1 = P[0:4]
P2 = P[4:8]
P3 = P[8:12]


def rotate90(P):
    rotatedP = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            rotatedP[j][3 - i] = P[i][j]
    return rotatedP


R0P1 = P1
R0P2 = P2
R1P2 = rotate90(R0P2)
R2P2 = rotate90(R1P2)
R3P2 = rotate90(R2P2)
R0P3 = P3
R1P3 = rotate90(R0P3)
R2P3 = rotate90(R1P3)
R3P3 = rotate90(R2P3)


def judge(p1, p2, p3, p1x, p1y, p2x, p2y, p3x, p3y):
    total = 0
    for y in range(4):
        for x in range(4):
            total += p1[y][x] + p2[y][x] + p3[y][x]
            s = 0
            if 0 <= x + p1x < 4 and 0 <= y + p1y < 4:
                s += p1[y + p1y][x + p1x]
            if 0 <= x + p2x < 4 and 0 <= y + p2y < 4:
                s += p2[y + p2y][x + p2x]
            if 0 <= x + p3x < 4 and 0 <= y + p3y < 4:
                s += p3[y + p3y][x + p3x]

            if s != 1:
                return False

    if total != 16:
        return False

    return True


for p1, p2, p3 in itertools.product([R0P1], [R0P2, R1P2, R2P2, R3P2], [R0P3, R1P3, R2P3, R3P3]):
    for p1x, p1y, p2x, p2y, p3x, p3y in itertools.product(range(-3, 4), repeat=6):
        if judge(p1, p2, p3, p1x, p1y, p2x, p2y, p3x, p3y):
            print("Yes")
            exit()

print("No")
