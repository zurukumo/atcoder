N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]


def judge(dy, dx):
    for y in range(M):
        for x in range(M):
            if S[y + dy][x + dx] != T[y][x]:
                return False

    return True


for y in range(N - M + 1):
    for x in range(N - M + 1):
        if judge(y, x):
            print(y + 1, x + 1)
            exit()
