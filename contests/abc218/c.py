import sys

sys.setrecursionlimit(10**7)

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def trim(area):
    while True:
        flag = False
        while all(c == "." for c in area[0]):
            area.pop(0)
            flag = True
        while all(c == "." for c in area[-1]):
            area.pop()
            flag = True
        while all(r[0] == "." for r in area):
            for i in range(len(area)):
                area[i].pop(0)
            flag = True
        while all(r[-1] == "." for r in area):
            for i in range(len(area)):
                area[i].pop()
            flag = True

        if not flag:
            break


def rotate(area):
    h = len(area)
    w = len(area[0])
    new_area = [[""] * h for _ in range(w)]
    for y in range(h):
        for x in range(w):
            new_area[w - x - 1][y] = area[y][x]
    return new_area


trim(S)
trim(T)


for _ in range(4):
    if len(S) == len(T) and len(S[0]) == len(T[0]):
        if all(s == t for s, t in zip(S, T)):
            print("Yes")
            exit()

    T = rotate(T)


print("No")
