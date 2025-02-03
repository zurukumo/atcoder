N, K = map(int, input().split())
H = [0] + [int(i) for i in input().split()]

dp = [[float('inf')] * (N - K + 1) for _ in range(N + 1)]
dp[0][0] = 0

# 右端がi、サイズがj
for i in range(1, N + 1) :
  for j in range(N - K + 1) :
    dp[i][j] = min(dp[k][j-1] + max(0, H[i] - H[k]) for k in range(i))

print(min(dp[i][N-K] for i in range(N + 1)))