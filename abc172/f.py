N = int(input())
A = [int(i) for i in input().split()]

S = A[0] + A[1]
X = 0
for i in range(2, N) :
  X ^= A[i]

dp = [[[-1] * 2 for _ in range(2)] for _ in range(60)]
dp[0][0][0] = 0

for i in range(59) :
  cs = (S >> i) & 1
  cx = (X >> i) & 1
  ca = (A[0] >> i) & 1
  for j in (0, 1) :
    for k in (0, 1) :
      if dp[i][j][k] < 0 : continue
      for na in (0, 1) :
        for nb in (0, 1) :
          ni = i + 1
          nj = 0
          nk = k
          if na ^ nb != cx : continue
          ns = na + nb + j
          if ns % 2 != cs :continue
          if ns >= 2 :
            nj = 1
          if ca < na :
            nk = 1
          elif ca == na :
            nk = k
          else :
            nk = 0
          dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (na << i))
          
if 1 <= dp[-1][0][0] <= A[0] :
  print(A[0] - dp[-1][0][0])
else :
  print(-1)