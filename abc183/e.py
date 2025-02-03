H, W = map(int, input().split())
S = [[i for i in input()] for _ in range(H)]

mod = 10 ** 9 + 7
dp = [[0] * W for _ in range(H)]
tate = [[0] * W for _ in range(H)]
yoko = [[0] * W for _ in range(H)]
naname = [[0] * W for _ in range(H)]

dp[0][0] = 1
tate[0][0] = 1
yoko[0][0] = 1
naname[0][0] = 1

for y in range(H) :
  for x in range(W) :
    if y == x == 0 :
      continue
    if S[y][x] == '#' :
      continue
    
    if y > 0 : 
      dp[y][x] += tate[y - 1][x]
      dp[y][x] %= mod
    if x > 0 : 
      dp[y][x] += yoko[y][x - 1]
      dp[y][x] %= mod
    if y > 0 and x > 0 : 
      dp[y][x] += naname[y - 1][x - 1]
      dp[y][x] %= mod
  
    tate[y][x] = dp[y][x]
    yoko[y][x] = dp[y][x]
    naname[y][x] = dp[y][x]
    
    if y > 0 : 
      tate[y][x] += tate[y - 1][x]
      tate[y][x] %= mod
    if x > 0 :
      yoko[y][x] += yoko[y][x - 1]
      yoko[y][x] %= mod
    if y > 0 and x > 0 : 
      naname[y][x] += naname[y - 1][x - 1]
      naname[y][x] %= mod
    
print(dp[-1][-1])