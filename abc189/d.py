N = int(input())
S = [input() for _ in range(N)]

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, N + 1) :
  if S[i - 1] == 'AND' :
    dp[i][0] += dp[i - 1][0] * 2 + dp[i - 1][1]
    dp[i][1] += dp[i - 1][1]
  else :
    dp[i][0] += dp[i - 1][0] 
    dp[i][1] += dp[i - 1][0] + dp[i - 1][1] * 2

print(dp[-1][1])