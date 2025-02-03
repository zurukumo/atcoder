N, S = map(int, input().split())
A = [int(i) for i in input().split()]

mod = 998244353

dp = [0] * (S + 1)
dp[0] = 1
for a in A :
  for i in range(S, -1, -1) :
    if i >= a :
      dp[i] = dp[i] * 2 + dp[i - a]
    else :
      dp[i] = dp[i] * 2
    dp[i] %= mod
print(dp[-1])