N = [int(i) for i in input()]

dp = [0, float('inf')]
# dp = [桁上げしてない, 桁上げあった]
for n in N :
  ndp = [0] * 2
  ndp[0] = min(dp[0] + n, dp[1] + n)
  ndp[1] = min(dp[0] + 11 - n, dp[1] + 9 - n)
  dp = ndp

print(min(dp[0], dp[1]))