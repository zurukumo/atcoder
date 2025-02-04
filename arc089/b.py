N, K = map(int, input().split())

dp = [[0] * (3 * K + 1) for _ in range(2 * K + 1)]
for _ in range(N):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == "W":
        x += K

    m = min(x // K, y // K)
    x -= m * K
    y -= m * K
    x %= 2 * K
    y %= 2 * K

    dp[x][y] += 1
    if x < K and y < K:
        dp[x + K][y + K] += 1
        dp[x][y + 2 * K] += 1
    elif x < K and y >= K:
        dp[x + K][y - K] += 1
        dp[x + K][y + K] += 1
    elif x >= K and y < K:
        dp[x - K][y + K] += 1
        dp[x][y + 2 * K] += 1

for i in range(2 * K):
    for j in range(3 * K):
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

ret = 0
for i in range(K - 1, 2 * K):
    for j in range(K - 1, 3 * K):
        ret = max(ret, dp[i][j] - dp[i][j - K] - dp[i - K][j] + dp[i - K][j - K])
print(ret)
