N = int(input())
S = [input() for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N)]
for i in range(N):
    rw = S[i].count(".")
    lb = 0
    dp[i][0] = rw + lb
    for j in range(N):
        if S[i][j] == ".":
            rw -= 1
        else:
            lb += 1

        dp[i][j + 1] = rw + lb


for i in range(N):
    for j in range(N, -1, -1):
        if i - 1 >= 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        if j + 1 < N + 1:
            dp[i][j] = min(dp[i][j], dp[i][j + 1])

print(dp[-1][0])
