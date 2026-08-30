import itertools
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

A = [[int(i) for i in input().split()] for _ in range(3)]


def judge(i, j, B):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for line in lines:
        if (i, j) in line:
            line.remove((i, j))
            if (
                B[line[0][0]][line[0][1]] != -1
                and B[line[1][0]][line[1][1]] != -1
                and B[line[0][0]][line[0][1]] == B[line[1][0]][line[1][1]]
            ):
                return True
    return False


gakkari = 0
for seq in itertools.permutations(range(9), 9):
    B = [[-1] * 3 for _ in range(3)]
    for x in seq:
        i, j = x // 3, x % 3
        if judge(i, j, B):
            gakkari += 1
            break
        B[i][j] = A[i][j]


patterns = 1
for i in range(1, 10):
    patterns *= i

print((patterns - gakkari) / patterns)
