import bisect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
PAB = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
X = [int(input()) for _ in range(Q)]

dp = [[0] * 1001 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    p, a, b = PAB[i]
    for j in range(1000 + 1):
        if j > p:
            dp[i][j] = dp[i + 1][max(0, j - b)] - min(j, b)
        else:
            dp[i][j] = dp[i + 1][j + a] + a

sumb = [0] * (N + 1)
for i, (p, a, b) in enumerate(PAB):
    sumb[i + 1] += sumb[i] + b

for x in X:
    i = bisect.bisect_right(sumb, x - 1000)
    if i > N:
        print(x - sumb[-1])
    else:
        x -= sumb[i]
        print(x + dp[i][x])
