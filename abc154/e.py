N = input()
K = int(input())

dp = [[0] * 4 for _ in range(2)]
dp[0][1] = 1
dp[1][0] = 1
dp[1][1] = int(N[0]) - 1

for n in N[1:] :
  n = int(n)
  ndp = [[0] * 4 for _ in range(2)]
  
  if n == 0 :
    ndp[0] = dp[0]
  else :
    ndp[0][1] = dp[0][0]
    ndp[0][2] = dp[0][1]
    ndp[0][3] = dp[0][2]

  ndp[1][0] = dp[1][0]
  ndp[1][1] = dp[1][1] + dp[1][0] * 9
  ndp[1][2] = dp[1][2] + dp[1][1] * 9
  ndp[1][3] = dp[1][3] + dp[1][2] * 9
    
  if n != 0 :
    ndp[1][0] += dp[0][0]
    ndp[1][1] += dp[0][0] * (n - 1) + dp[0][1]
    ndp[1][2] += dp[0][1] * (n - 1) + dp[0][2]
    ndp[1][3] += dp[0][2] * (n - 1) + dp[0][3]
  
  dp = ndp
  
print(dp[0][K] + dp[1][K])