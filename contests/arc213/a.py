import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, L = map(int, input().split())
CP = [[0, *list(range(1, L + 1))]] + [[int(i) for i in input().split()] for _ in range(N)]


def dist(x, y):
    d = 0
    lx = CP[x][1:]
    ly = CP[y][1:]
    for i in range(L):
        vx = lx[i]
        j = ly.index(vx)
        while i < j:
            ly[j - 1], ly[j] = ly[j], ly[j - 1]
            d += 1
            j -= 1

    return d


dp = [-float("inf")] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    for j in range(max(0, i - L**2), i):
        if dist(i, j) <= i - j:
            dp[i] = max(dp[i], dp[j] + CP[i][0])

print(max(dp))
