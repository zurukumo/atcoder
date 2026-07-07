import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
TB = [[int(i) for i in input().split()] for _ in range(Q)]

M = 35

pos = [[0] * N for _ in range(M)]
val = [[0] * N for _ in range(M)]

for i, a in enumerate(A):
    pos[0][i] = a - 1
    val[0][i] = i + 1

for i in range(M - 1):
    for j in range(N):
        pos[i + 1][j] = pos[i][pos[i][j]]
        val[i + 1][j] = val[i][j] + val[i][pos[i][j]]


for t, b in TB:
    b -= 1
    x = 0
    for i in range(M):
        if t & (1 << i):
            x += val[i][b]
            b = pos[i][b]
    print(x)
