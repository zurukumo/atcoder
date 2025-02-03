from collections import defaultdict

N = int(input())
C = [int(input())]
for _ in range(N - 1) :
  c = int(input())
  if c != C[-1] :
    C.append(c)

mod = 10 ** 9 + 7

ret = 1
dp = defaultdict(int)
for c in C :
  tmp = dp[c]
  dp[c] += ret
  ret += tmp
  dp[c] %= mod
  ret %= mod

print(ret)