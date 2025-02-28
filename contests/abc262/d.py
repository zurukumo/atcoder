N = int(input())
a = [int(i) for i in input().split()]

mod = 998244353

ret = 0
for n in range(1, N + 1):
    b = [v % n for v in a]
    dp = [[0] * n for _ in range(n + 1)]
    dp[0][0] = 1
    for v in b:
        for i in range(n, 0, -1):
            for j in range(n):
                dp[i][j] += dp[i - 1][(j - v) % n]
                dp[i][j] %= mod
    ret += dp[-1][0]
    ret %= mod
print(ret)
