W = int(input())
N, K = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[-float("inf")] * (W + 1) for _ in range(K + 1)]
dp[0][0] = 0
for A, B in AB:
    for i in range(K, 0, -1):
        for j in range(A, W + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - A] + B)

print(max(max(dp[i]) for i in range(K + 1)))
