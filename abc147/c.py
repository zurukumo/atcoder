import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
A = [[-1] * N for _ in range(N)]
for i in range(N):
    An = int(input())
    for _ in range(An):
        x, y = map(int, input().split())
        A[i][x - 1] = y


def check(honest):
    for i in range(N):
        for j in range(N):
            if honest[i] and (
                (honest[j] == 0 and A[i][j] == 1) or (honest[j] == 1 and A[i][j] == 0)
            ):
                return False

    return True


ret = 0
for i in range(2**N):
    honest = [0] * N
    for j in range(N):
        if i & 1:
            honest[j] = 1
        i //= 2

    if check(honest):
        ret = max(ret, sum(honest))

print(ret)
