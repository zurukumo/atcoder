H, W, N = map(int, input().split())
ab = [[int(i) - 1 for i in input().split()] for _ in range(N)]

dp = [[0] * W for _ in range(H)]
hole = [[0] * W for _ in range(H)]

for a, b in ab:
    dp[a][b] = 1
    hole[a][b] = 1

for i in range(H):
    for j in range(W):
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] -= dp[i - 1][j - 1]


def find_hole(x1, y1, x2, y2):
    if x1 == 0 and y1 == 0:
        return dp[x2][y2]
    elif x1 == 0:
        return dp[x2][y2] - dp[x2][y1 - 1]
    elif y1 == 0:
        return dp[x2][y2] - dp[x1 - 1][y2]
    else:
        return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]


ret = 0
for y in range(H):
    for x in range(W):
        if hole[y][x] == 1:
            continue
        ok = 0
        ng = min(H - y, W - x)

        while ng - ok > 1:
            mid = (ok + ng) // 2
            if find_hole(y, x, y + mid, x + mid) == 0:
                ok = mid
            else:
                ng = mid

        ret += ok + 1

print(ret)
