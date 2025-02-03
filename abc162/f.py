import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

#dp[i][done][extra]
if N % 2 == 0 :
  extra = 2
else :
  extra = 3
  
N += 1
A = A + [-float('inf')]
  
dp = [[[-float('inf')] * extra for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N) :
  a = A[i]
  for j in range(2) :
    for k in range(extra) :
      # 取る場合
      if j == 0 :
        dp[i+1][1][k] = max(dp[i+1][1][k], dp[i][j][k] + a)
      # 取らない場合
      if j == 1 :
        dp[i+1][0][k] = max(dp[i+1][0][k], dp[i][j][k])
      if j == 0 and k != extra - 1 :
        dp[i+1][0][k + 1] = max(dp[i+1][0][k + 1], dp[i][j][k])

# for dp_ in dp :
  # print(dp_)

print(max(dp[-1][0][-1], dp[-1][1][-1]))