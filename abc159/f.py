N, S = map(int, input().split())
A = [int(i) for i in input().split()]

mod = 998244353

dp = [[0] * (S + 1) for _ in range(N + 1)]

ret = 0
for i, a in enumerate(A):
    if a <= S:
        dp[i + 1][a] += i + 1

    for j in range(S, -1, -1):
        dp[i + 1][j] += dp[i][j]
        if j >= a:
            dp[i + 1][j] += dp[i][j - a]
        dp[i + 1][j] %= mod

    ret += (dp[i + 1][S] - dp[i][S]) * (N - i) % mod
    ret %= mod

print(ret)
