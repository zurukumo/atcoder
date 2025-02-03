N = int(input())
D = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
P = [int(input()) for _ in range(Q)]

dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N) :
  for j in range(N) :
    dp[i+1][j+1] = D[i][j]

for i in range(1, N + 1) :
  for j in range(1, N + 1) :
    dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

ret = [0] * (N * N + 1)
for ai in range(1, N + 1) :
  for aj in range(1, N + 1) :
    for bi in range(ai, N + 1) :
      for bj in range(aj, N + 1) :
        s = (bj - aj + 1) * (bi - ai + 1)
        ret[s] = max(ret[s], dp[bj][bi] - dp[bj][ai-1] - dp[aj-1][bi] + dp[aj-1][ai-1])

for i in range(1, N * N + 1) :
  ret[i] = max(ret[i], ret[i-1])

for p in P :
  print(ret[p])