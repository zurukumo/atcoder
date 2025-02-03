N, K = map(int, input().split())
LR = [[int(i) for i in input().split()] for _ in range(K)]

mod = 998244353
dp = [0] * (N + K + 10)
diff = [0] * (N + K + 10)

dp[1] = diff[1] = 1
diff[2] = -1
for i in range(1, N + 1) :
  dp[i] = dp[i - 1] + diff[i]
  dp[i] %= mod
  for L, R in LR :
    if i + L <= N :
      diff[i + L] += dp[i]
      diff[i + L] %= mod
    if i + R + 1 <= N :
      diff[i + R + 1] -= dp[i]
      diff[i + R + 1] %= mod
  
print(dp[N])