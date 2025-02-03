import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N + 1):
    for j in range(M + 1):
        if i < N:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
        if j < M:
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

        if i < N and j < M:
            if A[i] == B[j]:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)

print(dp[N][M])
