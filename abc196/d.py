import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

H, W, A, B = map(int, input().split())

ret = 0
field = [[0] * W for _ in range(H)]


def dfs(A, B):
    s = 0
    for r in field:
        s += sum(r)
    if s == H * W and A == 0 and B == 0:
        global ret
        ret += 1
        return

    for y in range(H):
        for x in range(W):
            if field[y][x] == 0:
                if y + 1 < H and field[y + 1][x] == 0 and A > 0:
                    field[y][x] = 1
                    field[y + 1][x] = 1
                    dfs(A - 1, B)
                    field[y][x] = 0
                    field[y + 1][x] = 0

                if x + 1 < W and field[y][x + 1] == 0 and A > 0:
                    field[y][x] = 1
                    field[y][x + 1] = 1
                    dfs(A - 1, B)
                    field[y][x] = 0
                    field[y][x + 1] = 0

                if B > 0:
                    field[y][x] = 1
                    dfs(A, B - 1)
                    field[y][x] = 0

                return


dfs(A, B)
print(ret)
