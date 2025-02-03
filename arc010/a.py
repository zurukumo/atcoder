n, m, Y, Z = map(int, input().split())
cp = dict()
cn = dict()
for i in range(m) :
  c, p = input().split()
  cp[c] = int(p)
  cn[c] = i
b = input()

dp = [[-float('inf')] * (1 << m) for _ in range(m)]
for i in range(m) :
  dp[i][0] = 0
  
for color in b :
  p = cp[color]
  ni = cn[color]
  
  ndp = [[0] * (1 << m) for _ in range(m)]
  for i in range(m) :
    for j in range(1 << m) :
      ndp[i][j] = dp[i][j]

  for i in range(m) :
    for j in range(1 << m) :
      nj = j | (1 << ni)
      if i == ni and j != 0 :
        ndp[ni][nj] = max(ndp[ni][nj], dp[i][j] + p + Y)
      else :
        ndp[ni][nj] = max(ndp[ni][nj], dp[i][j] + p)
  dp = ndp
  
for i in range(m) :
  dp[i][-1] += Z
  
print(max(max(dp[i]) for i in range(m)))