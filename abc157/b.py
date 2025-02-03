A = [[int(i) for i in input().split()] for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]


def check():
    bingo = [[False] * 3 for _ in range(3)]

    for y in range(3):
        for x in range(3):
            if A[y][x] in b:
                bingo[y][x] = True

    # TATE
    for x in range(3):
        if bingo[0][x] and bingo[1][x] and bingo[2][x]:
            return True

    # YOKO
    for y in range(3):
        if bingo[y][0] and bingo[y][1] and bingo[y][2]:
            return True

    # NANAME
    if bingo[0][0] and bingo[1][1] and bingo[2][2]:
        return True
    if bingo[0][2] and bingo[1][1] and bingo[2][0]:
        return True

    return False


if check():
    print('Yes')
else:
    print('No')
