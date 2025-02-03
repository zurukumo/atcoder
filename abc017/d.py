N, M = map(int, input().split())
f = [int(input()) for _ in range(N)]
mod = 10 ** 9 + 7

dp = [0] * (N + 1)
s = [0] * (N + 1)
cnt = [0] * (M + 1)
dp[0] = s[0] = 1

fr = 0
for i, v in enumerate(f) :
  cnt[v] += 1
  while cnt[v] > 1 :
    cnt[f[fr]] -= 1
    fr += 1
  dp[i+1] = (s[i] - s[fr-1]) % mod
  s[i+1] = (s[i] + dp[i+1]) % mod

print(dp[-1])