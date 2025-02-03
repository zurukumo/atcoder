N, X = map(int, input().split())
A = [int(i) for i in input().split()]

ret = float('inf')
for K in range(1, N + 1) :
  dp = [[-float('inf')] * (K + 1) for _ in range(K + 1)]
  dp[0][0] = 0
  for a in A :
    for i in range(K - 1, -1, -1) :
      for j in range(K + 1) :
        dp[i + 1][(j + a) % K] = max(dp[i + 1][(j + a) % K], dp[i][j] + a)
  
  s = dp[K][X % K]
  if s == -float('inf') :
    continue
  ret = min(ret, (X - s) // K)
  
print(ret)