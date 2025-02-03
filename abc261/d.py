N, M = map(int, input().split())
X = [int(i) for i in input().split()]
CY = [[int(i) for i in input().split()] for _ in range(M)]

dp = [[-float("inf")] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

bonus = [0] * (N + 1)
for c, y in CY:
    bonus[c] = y

for i in range(N + 1):
    for j in range(N + 1):
        if i + 1 <= N and j + 1 <= N:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + bonus[j + 1] + X[i])
        if i + 1 <= N:
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])


print(max(dp[N]))
