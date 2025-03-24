N = int(input())

M = len(str(N))

# dp[consecutive][now consecutive][equal(0) or less(1)]
dp = [[[0] * 2 for _ in range(2)] for _ in range(M + 1)]
for i, c in enumerate(str(N)):
    if i == 0:
        dp[0][1][0] += 1
    else:
        dp[0][1][1] += 1

    c = int(c)
    ndp = [[[0] * 2 for _ in range(2)] for _ in range(M + 1)]
    for consecutive in range(M):
        for nc in range(10):
            if nc < c:
                if nc == 1:
                    ndp[consecutive][0][1] += dp[consecutive][0][0]
                    ndp[consecutive][0][1] += dp[consecutive][0][1]
                    ndp[consecutive + 1][1][1] += dp[consecutive][1][0]
                    ndp[consecutive + 1][1][1] += dp[consecutive][1][1]
                else:
                    ndp[consecutive][0][1] += dp[consecutive][0][0]
                    ndp[consecutive][0][1] += dp[consecutive][0][1]
                    ndp[consecutive][0][1] += dp[consecutive][1][0]
                    ndp[consecutive][0][1] += dp[consecutive][1][1]
            elif nc == c:
                if nc == 1:
                    ndp[consecutive][0][0] += dp[consecutive][0][0]
                    ndp[consecutive][0][1] += dp[consecutive][0][1]
                    ndp[consecutive + 1][1][0] += dp[consecutive][1][0]
                    ndp[consecutive + 1][1][1] += dp[consecutive][1][1]
                else:
                    ndp[consecutive][0][0] += dp[consecutive][0][0]
                    ndp[consecutive][0][1] += dp[consecutive][0][1]
                    ndp[consecutive][0][0] += dp[consecutive][1][0]
                    ndp[consecutive][0][1] += dp[consecutive][1][1]
            elif nc > c:
                if nc == 1:
                    ndp[consecutive][0][1] += dp[consecutive][0][1]
                    ndp[consecutive + 1][1][1] += dp[consecutive][1][1]
                else:
                    ndp[consecutive][0][1] += dp[consecutive][0][1]
                    ndp[consecutive][0][1] += dp[consecutive][1][1]
    dp = ndp

ret = 0
for consecutive in range(M + 1):
    for now_consecutive in range(2):
        for equal in range(2):
            ret += dp[consecutive][now_consecutive][equal] * consecutive
print(ret)
