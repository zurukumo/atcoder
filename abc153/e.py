import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

H, N = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]
AB.sort(key=lambda x: x[0]/x[1], reverse=True)

INF = 10 ** 18
dp = [INF] * (H + 1)
dp[0] = 0
for A, B in AB :
  for i in range(H + 1) :
    if dp[i] != INF :
      ni = min(H, i + A)
      dp[ni] = min(dp[ni], dp[i] + B)
      
print(dp[-1])