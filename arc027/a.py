X, Y = map(int, input().split())
N = int(input())
th = [[int(i) for i in input().split()] for _ in range(N)]

for i in range(N) :
  th[i][0] -= 1

dp = [[-1] * (X + Y + 1) for _ in range(X + 1)]
dp[0][0] = 0

for t, h in th :
  for i in range(X - 1, -1, -1) :
    for j in range(X + Y + 1) :
      if j + t > X + Y or dp[i][j] < 0 :
        continue
      dp[i + 1][j + t] = max(dp[i + 1][j + t], dp[i][j] + h)

for i in range(1, X + Y + 1) :
  dp[0][i] = max(dp[0][i], dp[0][i-1])
for i in range(1, X + 1) :
  dp[i][0] = max(dp[i][0], dp[i-1][0])
for i in range(1, X + 1) :
  for j in range(1, X + Y + 1) :
    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

ret = 0
for x in range(X + 1) :
  y = X + Y - x
  ret = max(ret, dp[x][y])

print(ret)