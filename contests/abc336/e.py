N = int(input())

ns = []
while N > 0:
    ns.append(N % 10)
    N //= 10
ns.reverse()


M = 9 * 14

ret = 0
for mod in range(1, M + 1):
    # dp[ketawa][mod][same]
    dp = [[[0] * 2 for _ in range(mod + 1)] for _ in range(mod + 1)]
    dp[0][0][1] = 1
    for n in ns:
        ndp = [[[0] * 2 for _ in range(mod + 1)] for _ in range(mod + 1)]
        for i in range(mod + 1):
            for j in range(mod + 1):
                for k in range(2):
                    for d in range(10):
                        if k == 0 or (k == 1 and d < n):
                            ni = i + d
                            nj = (j * 10 + d) % mod
                            nk = 0
                            if ni <= mod:
                                ndp[ni][nj][nk] += dp[i][j][k]
                        if k == 1 and d == n:
                            ni = i + d
                            nj = (j * 10 + d) % mod
                            nk = 1
                            if ni <= mod:
                                ndp[ni][nj][nk] += dp[i][j][k]
        dp = ndp

    ret += dp[mod][0][0] + dp[mod][0][1]
print(ret)
