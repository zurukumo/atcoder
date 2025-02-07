N, M = map(int, input().split())

mod = 998244353

patterns = []
i = 1
while i <= M:
    patterns.append(i)
    M -= i
    i *= 2

if M > 0:
    patterns.append(M)


dp = [0] * (len(patterns) + 1)
dp[0] = 1
for p in patterns:
    for i in range(len(patterns), -1, -1):
        dp[i] += dp[i - 1] * p
        dp[i] %= mod

if len(dp) > N:
    print(dp[N])
else:
    print(0)
