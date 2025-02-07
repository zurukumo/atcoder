N, A = map(int, input().split())
x = [int(i) for i in input().split()]

ax = [i - A for i in x]
p, m = 0, 0

for i in ax:
    if i > 0:
        p += i
    else:
        m -= i

dp = [[0] * (p + m + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(p + m + 1):
        dp[i + 1][(j + ax[i]) % (p + m + 1)] += dp[i][j]
        dp[i + 1][j] += dp[i][j]

print(dp[N][0] - 1)
