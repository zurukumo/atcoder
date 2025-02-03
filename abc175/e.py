R, C, K = map(int, input().split())
xy = [[0] * (C + 1) for _ in range(R + 1)]
for _ in range(K) :
  r, c, v = map(int, input().split())
  xy[r - 1][c - 1] = v

dp = [[[0] * (C + 1) for _ in range(R + 1)] for _ in range(4)]
for cy in range(R + 1) :
  for cx in range(C + 1) :
    if cx < C :
      dp[0][cy][cx + 1] = max(dp[0][cy][cx + 1], dp[0][cy][cx])
      dp[1][cy][cx + 1] = max(dp[1][cy][cx + 1], dp[0][cy][cx] + xy[cy][cx], dp[1][cy][cx])
      dp[2][cy][cx + 1] = max(dp[2][cy][cx + 1], dp[1][cy][cx] + xy[cy][cx], dp[2][cy][cx])
      dp[3][cy][cx + 1] = max(dp[3][cy][cx + 1], dp[2][cy][cx] + xy[cy][cx], dp[3][cy][cx])
    if cy < R :
      dp[0][cy + 1][cx] = max(dp[i][cy][cx] for i in range(3)) + xy[cy][cx]
      dp[0][cy + 1][cx] = max(dp[0][cy + 1][cx], dp[3][cy][cx])

print(max(dp[i][-1][-1] for i in range(4)))