N = int(input())
X, Y = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[float("inf")] * (Y + 1) for _ in range(X + 1)]
dp[0][0] = 0

for a, b in AB:
    for x in range(X, -1, -1):
        for y in range(Y, -1, -1):
            nx = min(X, x + a)
            ny = min(Y, y + b)
            dp[nx][ny] = min(dp[nx][ny], dp[x][y] + 1)

if dp[-1][-1] == float("inf"):
    print(-1)
else:
    print(dp[-1][-1])
