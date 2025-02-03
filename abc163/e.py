N = int(input())
A = [int(i) for i in input().split()]

ap = [(v, k) for k, v in enumerate(A)]
ap.sort(reverse=True)

dp = [[-float('inf')] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i, (a, p) in enumerate(ap) :
  for l in range(i + 1) :
    r = i - l
    if l + 1 <= N :
      dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + a * (p - l))
    if r + 1 <= N :
      dp[l][r + 1] = max(dp[l][r + 1], dp[l][r] + a * (N - 1 - r - p))
  
print(max(dp[i][N - i] for i in range(N + 1)))