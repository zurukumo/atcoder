import sys

input = sys.stdin.readline

H, W = map(int, input().split())
A = [[1 if i == "+" else -1 for i in input()] for _ in range(H)]

dp = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if (y + x) % 2 == 0:
            dp[y][x] = float("inf")
        else:
            dp[y][x] = -float("inf")
dp[-1][-1] = 0

for y in range(H - 1, -1, -1):
    for x in range(W - 1, -1, -1):
        who = (x + y) % 2
        if y > 0:
            if who == 0:
                dp[y - 1][x] = max(dp[y][x] + A[y][x], dp[y - 1][x])
            else:
                dp[y - 1][x] = min(dp[y][x] - A[y][x], dp[y - 1][x])

        if x > 0:
            if who == 0:
                dp[y][x - 1] = max(dp[y][x] + A[y][x], dp[y][x - 1])
            else:
                dp[y][x - 1] = min(dp[y][x] - A[y][x], dp[y][x - 1])

    # for dp_ in dp:
    #     print(dp_)
    # print()

if dp[0][0] < 0:
    print("Takahashi")
elif dp[0][0] > 0:
    print("Aoki")
else:
    print("Draw")
